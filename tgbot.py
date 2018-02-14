# See LICENSE file for copyright and license details.

import json
import os
from pathlib import Path

from aiotg import Bot

from config import MATERIAS
from util import slugify

bot = Bot(os.environ["TELEGRAM_BOT_TOKEN"])


@bot.command(r'/start')
def start(chat, match):

    markup = {
            'type': 'InlineKeyboardMarkup',
            'inline_keyboard': [
                [{'type': 'InlineKeyboardButton',
                    'text': name,
                    'callback_data': 'biblio-' + slugify(name)} for name, _ in MATERIAS
                  ],
                ]
            }

    chat.send_text('Materias:', reply_markup=json.dumps(markup))


@bot.callback(r'biblio-(.*)')
def buttonclick(chat, cq, match):
    cq.answer()
    materia = match.group(1)

    root = Path(materia)
    if not root.exists():
        chat.send_text('No existe la materia {}'.format(materia))
        return

    biblio = root / 'bibliografia.md'
    if not biblio.exists():
        chat.send_text('La materia {} no tiene bibliografía'.format(materia))
        return

    with biblio.open() as f:
        markdown = f.read()
        chat.send_text(markdown, parse_mode='markdown')



@bot.callback
def unhandled_callback(chat, cq):
    cq.answer()
    chat.send_text('?')


bot.run(debug=True)
