# See LICENSE file for copyright and license details.

.PHONY: dl
dl:
	pipenv run python dl.py

.PHONY: bot
bot:
	pipenv run python tgbot.py
