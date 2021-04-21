
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.db_api import db_game, db_orgs, db_code, db_hint
from aiogram.utils.callback_data import CallbackData

hint_all_cd = CallbackData("hint", "a", "hid", "mid")

async def get_all_hint_keyboard(mission_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    hint_all_id = await db_hint.get_all_id(mission_id)
    print(mission_id, "keyboard hint all")

    if len(hint_all_id) > 0:
        for hint_id in hint_all_id:
            hint_title = await db_hint.get_title(hint_id)
            keyboard.insert(InlineKeyboardButton(text=hint_title,
                                                 callback_data=hint_all_cd.new(a="set", hid=hint_id, mid=mission_id)))

    keyboard.insert(InlineKeyboardButton(text="Добавить",
                                         callback_data=hint_all_cd.new(a="add", hid=0, mid=mission_id)))

    keyboard.insert(InlineKeyboardButton(text="Назад",
                                         callback_data=hint_all_cd.new(a="back", hid=0, mid=mission_id)))
    return keyboard


hint_setting_cd = CallbackData("set", "a", "hid" )
async def get_setting_hint_keyboard(hint_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.insert(InlineKeyboardButton(text="Просмотр", callback_data=hint_setting_cd.new(a="show", hid=hint_id)))
    keyboard.insert(InlineKeyboardButton(text="Название", callback_data=hint_setting_cd.new(a="title", hid=hint_id)))
    keyboard.insert(InlineKeyboardButton(text="Описание", callback_data=hint_setting_cd.new(a="des", hid=hint_id)))
    keyboard.insert(InlineKeyboardButton(text="Превью", callback_data=hint_setting_cd.new(a="capt", hid=hint_id)))
    keyboard.insert(InlineKeyboardButton(text="Время", callback_data=hint_setting_cd.new(a="time", hid=hint_id)))
    keyboard.insert(InlineKeyboardButton(text="Удалить", callback_data=hint_setting_cd.new(a="del", hid=hint_id)))
    keyboard.insert(InlineKeyboardButton(text="Назад", callback_data=hint_setting_cd.new(a="back", hid=hint_id)))
    return keyboard