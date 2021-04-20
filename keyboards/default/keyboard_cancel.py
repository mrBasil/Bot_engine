
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def get_keybord_cancel():
    keyboard = ReplyKeyboardMarkup(True)
    keyboard.insert(KeyboardButton(text="отмена"))
    return keyboard