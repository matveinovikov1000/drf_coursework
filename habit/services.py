import requests

from config.settings import TG_BOT_TOKEN, TG_URL


def send_tg_message(message, chat_id):
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.get(f"{TG_URL}{TG_BOT_TOKEN}/sendMessage", params=params)
