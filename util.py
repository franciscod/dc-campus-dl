# See LICENSE file for copyright and license details.

import re
from unicodedata import normalize

import unidecode

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},:]+')

def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []
    for word in _punct_re.split(unidecode.unidecode(text).lower()):
        word = normalize('NFKD', word)
        if word:
            result.append(word)

    return delim.join(result)
