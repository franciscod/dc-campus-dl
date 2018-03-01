# See LICENSE file for copyright and license details.

import hashlib
import os
import shutil
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from html2text import HTML2Text
from rfc6266 import parse_headers

from config import MATERIAS
from util import slugify

HASH_BUF_SIZE = 65536
OLD_BASE_DIR = '.old'

class MoodleDL:
    def __init__(self, base_url='https://campus.exactas.uba.ar/'):
        self._session = requests.session()
        self._base_url = base_url

    def head(self, url, *args, **kwargs):
        if not url.startswith('http'):
            url = self._base_url + url

        return self._session.head(url, *args, **kwargs)

    def get(self, url, *args, **kwargs):
        if not url.startswith('http'):
            url = self._base_url + url

        return self._session.get(url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        if not url.startswith('http'):
            url = self._base_url + url

        return self._session.post(url, *args, **kwargs)

    def etag_sha1_matches(self, url, filename):
        # assumes ETag is the SHA1 of the file
        res = self.head(url, allow_redirects=True)
        etag = res.headers.get('ETag')

        if not etag:
            for r in res.history:
                etag = r.headers.get('ETag')
                if etag:
                    break
            else:
                print('No ETag on headers', filename, url)
                return False

        if not Path(filename).exists():
            print('File not previously downloaded', filename, url)
            return False

        sha1 = hashlib.sha1()
        with open(filename, 'rb') as f:
            while True:
                data = f.read(HASH_BUF_SIZE)
                if not data:
                    break
                sha1.update(data)
        digest = sha1.hexdigest()

        if not digest == etag:
            print('Digest and ETag mismatch', filename, url)
            print(digest, etag_sha1_matches)
            return False

        return True

    def download_file(self, url, filename):
        old_filename = os.path.join(OLD_BASE_DIR, filename)
        if self.etag_sha1_matches(url, old_filename):
            os.rename(old_filename, filename)
            return

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
        path = self.base_path()
        old_path = os.path.join(OLD_BASE_DIR, path)
        if os.path.isdir(path):
            if os.path.isdir(old_path):
                shutil.rmtree(old_path)
            os.makedirs(old_path, exist_ok=True)
            os.rename(path, old_path)

    def fetch_section(self, res):
        soup = self.bs(res.text)
        title = soup.select('.here span')[0].text
        content_soup = soup.select('#region-main .content')[0]
        h = HTML2Text(baseurl='')
        h.ul_item_mark = '-'
        content = h.handle(content_soup.prettify())
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
