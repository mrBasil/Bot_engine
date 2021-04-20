
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.db_api import db_game, db_orgs, db_code
from aiogram.utils.callback_data import CallbackData


code_all = CallbackData("code", "a", "gid", "mid", "cid")

async def all_code_keyboard(mission_id, game_id):
    keyboard = InlineKeyboardMarkup(row_width=2)

    code_all_id = await db_code.get_all_id(mission_id)
    i=0
    if len(code_all_id)>0:
        for code_id in code_all_id:
            i=i+1
            keyboard.insert(InlineKeyboardButton(text=f"code # {i}",
                                                 callback_data=code_all.new(a="set", mid=mission_id, gid=game_id, cid=code_id)))
    keyboard.insert(InlineKeyboardButton(text="Добавить",
                                         callback_data=code_all.new(a="add", mid=mission_id, gid=game_id, cid=0)))

    keyboard.insert(InlineKeyboardButton(text="Назад",
                                         callback_data=code_all.new(a="back", mid=mission_id, gid=game_id, cid=0)))
    return keyboard

code_set = CallbackData("c_set", "a", "cid")
async def set_codes_keyboard(code_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.insert(InlineKeyboardButton(text="Просмотр", callback_data=code_set.new(a="show", cid=code_id)))
    keyboard.insert(InlineKeyboardButton(text="Код", callback_data=code_set.new(a="code", cid=code_id)))
    keyboard.insert(InlineKeyboardButton(text="Тип", callback_data=code_set.new(a="type", cid=code_id)))
    keyboard.insert(InlineKeyboardButton(text="Бонус", callback_data=code_set.new(a="bonus", cid=code_id)))
    keyboard.insert(InlineKeyboardButton(text="Комментарий", callback_data=code_set.new(a="comm", cid=code_id)))
    keyboard.insert(InlineKeyboardButton(text="Удалить", callback_data=code_set.new(a="del", cid=code_id)))
    keyboard.insert(InlineKeyboardButton(text="Назад", callback_data=code_set.new(a="back", cid=code_id)))
    return keyboard