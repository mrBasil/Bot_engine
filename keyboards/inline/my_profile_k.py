
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.db_api import db_game, db_orgs
from aiogram.utils.callback_data import CallbackData

menu_profile = CallbackData("profile", "a", "id")

def get_my_profil_settings(user_id):

    '''
    show - показать игру
    login
    pass
    name
    family
    city
    team
    back
    '''

    key = InlineKeyboardMarkup(row_width=2)
    key.insert(InlineKeyboardButton(text="Просмотр профиля", callback_data=menu_profile.new(a="show", id=user_id)))
    key.insert(InlineKeyboardButton(text="LOGIN", callback_data=menu_profile.new(a="login", id=user_id)))
    key.insert(InlineKeyboardButton(text="PASSWORD", callback_data=menu_profile.new(a="pass", id=user_id)))
    key.insert(InlineKeyboardButton(text="Имя", callback_data=menu_profile.new(a="name", id=user_id)))
    key.insert(InlineKeyboardButton(text="Фамилия", callback_data=menu_profile.new(a="family", id=user_id)))
    key.insert(InlineKeyboardButton(text="Город", callback_data=menu_profile.new(a="city", id=user_id)))
    key.insert(InlineKeyboardButton(text="Команда", callback_data=menu_profile.new(a="team", id=user_id)))
    key.insert(InlineKeyboardButton(text="Назад", callback_data=menu_profile.new(a="back", id=user_id)))
    return key

menu_profile_tem = CallbackData("pt", "a", "id")
