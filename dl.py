import os
import re
import shutil
import sys
from unicodedata import normalize

import requests
from bs4 import BeautifulSoup
import html2text
import unidecode

from rfc6266 import parse_headers

"""
(nombre, id en el campus),
Por ejemplo, el link a PLP es:
https://campus.exactas.uba.ar/course/view.php?id=1059 <--- id!
"""
MATERIAS = (
    ('PLP', 1059),
    ('Algebra 1', 1095),
    ('LyC', 1057),
)


_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},:]+')

def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []
    for word in _punct_re.split(unidecode.unidecode(text).lower()):
        word = normalize('NFKD', word)
        if word:
            result.append(word)

    return delim.join(result)

class MoodleDL:
    def __init__(self, base_url='https://campus.exactas.uba.ar/'):
        self._session = requests.session()
        self._base_url = base_url

    def get(self, url, *args, **kwargs):
        if not url.startswith('http'):
            url = self._base_url + url

        return self._session.get(url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        if not url.startswith('http'):
            url = self._base_url + url

        return self._session.post(url, *args, **kwargs)

    def download_file(self, url, filename):
        data = self.get(url).content
        with open(filename, 'wb') as f:
            f.write(data)

    def bs(self, markup):
        return BeautifulSoup(markup, 'html.parser')

    def login(self, username='guest', password='guest'):
        return self.post('login/index.php', data={
            'action': 'login',
            'username': username,
            'password': password,
        })

    def agree_policy(self, res):
        return self.post('user/policy.php', data={
            'sesskey': self.bs(res.text).select('#region-main form input[name=sesskey]')[0]['value'],
            'agree': '1'
        })

    def fetch_course(self, course_name, course_id):
        self._course_name = course_name
        self.rename_old()

        # get course main page
        res = self.get('course/view.php?id=%s' % course_id)

        # handle policy
        if 'policy' in res.url:
            res = self.agree_policy(res)

        self.fetch_section(res)
        for a in self.bs(res.text).select('.tabtree li a'):
            href = a.get('href')
            if href:
                self.fetch_section(self._session.get(href))

    def base_path(self):
        return slugify(self._course_name)

    def path(self, filename, *dir_parts):
        path = os.path.join(self.base_path(), *dir_parts)
        os.makedirs(path, exist_ok=True)
        return os.path.join(path, filename)

    def rename_old(self):
        OLD_BASE = '.old'
        path = self.base_path()
        if os.path.isdir(path):
            if os.path.isdir(OLD_BASE):
                shutil.rmtree(OLD_BASE)
            os.makedirs(OLD_BASE, exist_ok=True)
            os.rename(path, os.path.join(OLD_BASE, path))

    def fetch_section(self, res):
        soup = self.bs(res.text)
        title = soup.select('.here span')[0].text
        content_soup = soup.select('#region-main .content')[0]

        content = html2text.html2text(content_soup.prettify())
        if content.strip() != '':
            with open(self.path(slugify(title) + '.md'), 'w') as f:
                f.write('# ' + title + '\n([fuente](' + res.url + '))\n---\n')
                f.write(content)

        for a in content_soup.select('a'):
            href = a.get('href')
            if not href:
                continue

            if '/mod/resource' in href:
                self.fetch_resource(href, slugify(title))

    def fetch_resource(self, url, basedir):
        res = self.get(url)
        content_disp = res.headers.get('Content-Disposition')
        if content_disp:
            cd = parse_headers(content_disp)
            dl_url, dl_name = url, cd.filename_unsafe
        else:
            # assuming 'regular' moodle resource page
            soup = self.bs(res.text)
            a = soup.select('object a')[0]
            dl_url = href =  a['href']
            dl_name = href.split('/')[-1]

        self.download_file(dl_url, self.path(dl_name, 'files_' + basedir))


if __name__ == '__main__':
    dl = MoodleDL()
    dl.login()

    for args in MATERIAS:
        dl.fetch_course(*args)
