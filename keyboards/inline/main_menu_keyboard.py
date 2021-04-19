
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import URL_CHANEL_MQ
from utils.db_api import db_game

async def getMenu():

    key = InlineKeyboardMarkup(row_width=2)
    key.insert(InlineKeyboardButton(text="Мета Квест", url=URL_CHANEL_MQ))
    key.insert(InlineKeyboardButton(text="Твой профиль", callback_data="my_profile"))
    key.insert(InlineKeyboardButton(text="Твой игры", callback_data="my_games"))

    return key