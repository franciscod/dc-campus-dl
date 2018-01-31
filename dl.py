import os
import re
import sys
from unicodedata import normalize

import requests
from bs4 import BeautifulSoup
import html2text
import unidecode


"""
(nombre, id en el campus),
Por ejemplo, el link a PLP es:
https://campus.exactas.uba.ar/course/view.php?id=1059 <--- id!
"""
MATERIAS = (
    ('PLP', 1059),
)


_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},]+')

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
        global ses
        self._session = requests.session()
        self._base_url = base_url
        ses = self._session

    def get(self, url, *args, **kwargs):
        if not url.startswith('http'):
            url = self._base_url + url

        return self._session.get(url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        if not url.startswith('http'):
            url = self._base_url + url

        return self._session.post(url, *args, **kwargs)

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

    def path(self, filename, *dir_parts):
        path = os.path.join('materias', slugify(self._course_name), *dir_parts)
        os.makedirs(path, exist_ok=True)
        return os.path.join(path, filename)

    def fetch_section(self, res):
        global soup, content_soup, content
        soup = self.bs(res.text)
        title = soup.select('.here span')[0].text
        content_soup = soup.select('#region-main .content')[0]

        content = html2text.html2text(content_soup.prettify())

        with open(self.path(slugify(title) + '.md', 'secciones'), 'w') as f:
            f.write('# ' + title + '\n([fuente](' + res.url + '))\n---\n')
            f.write(content)

        for a in content_soup.select('a'):
            href = a.get('href')
            if not href:
                continue

            if '/mod/resource' in href:
                self.fetch_resource(href, slugify(title))

    def fetch_resource(self, url, basedir):
        global r, soup, obj
        r = res = self.get(url)
        soup = self.bs(res.text)
        a = soup.select('object a')[0]
        href = a['href']

        filename = href.split('/')[-1]
        data = self.get(href).content
        with open(self.path(filename, 'descargas', basedir), 'wb') as f:
            f.write(data)

if __name__ == '__main__':
    dl = MoodleDL()
    dl.login()

    for args in MATERIAS:
        dl.fetch_course(*args)
