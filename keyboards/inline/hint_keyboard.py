
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.db_api import db_game, db_orgs, db_code, db_hint
from aiogram.utils.callback_data import CallbackData

async def get_all_hint(mission_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    hint_all_id = await db_hint
