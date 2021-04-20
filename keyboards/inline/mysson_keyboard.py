
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.db_api import db_game, db_orgs, db_mission
from aiogram.utils.callback_data import CallbackData


mission_add = CallbackData("miss", "a", "gid", "mid")
'''
gid -  game_id
mid -  mission_id
'''
async def get_all_mission(game_id):

    id_m = await db_mission.get_all_id(game_id)

    key = InlineKeyboardMarkup(row_width=2)
    if len(id_m)>0:
        for i in id_m:
            title = await db_mission.get_title(i)
            key.insert(InlineKeyboardButton(text=title, callback_data=mission_add.new(a="set", gid=game_id, mid=i)))
    key.insert(InlineKeyboardButton(text="Добавить", callback_data=mission_add.new(a="add", gid=game_id, mid=1)))
    key.insert(InlineKeyboardButton(text="Назад", callback_data=mission_add.new(a="back", gid=game_id, mid=1)))
    return key

mission = CallbackData("set", "a", "gid", "mid")
async def get_setting_mission(mission_id, game_id):
    '''

    :param mission_id:
    :param game_id:
    keyboard :return:

     title
     des
     del
     capt
     time
     code
     hint


    '''
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.insert(
        InlineKeyboardButton(text="Просмотр", callback_data=mission.new(a="show", gid=game_id, mid=mission_id)))

    keyboard.insert(InlineKeyboardButton(text="Название", callback_data=mission.new(a="title", gid=game_id, mid=mission_id)))
    keyboard.insert(
        InlineKeyboardButton(text="Описание", callback_data=mission.new(a="des", gid=game_id, mid=mission_id)))
    keyboard.insert(
        InlineKeyboardButton(text="Картинка", callback_data=mission.new(a="capt", gid=game_id, mid=mission_id)))
    keyboard.insert(
        InlineKeyboardButton(text="Автопереход", callback_data=mission.new(a="time", gid=game_id, mid=mission_id)))
    keyboard.insert(
        InlineKeyboardButton(text="Номер", callback_data=mission.new(a="num", gid=game_id, mid=mission_id)))
    keyboard.insert(
        InlineKeyboardButton(text="Коды", callback_data=mission.new(a="code", gid=game_id, mid=mission_id)))
    keyboard.insert(
        InlineKeyboardButton(text="Подсказки", callback_data=mission.new(a="hint", gid=game_id, mid=mission_id)))
    keyboard.insert(
        InlineKeyboardButton(text="Удалить", callback_data=mission.new(a="del", gid=game_id, mid=mission_id)))
    keyboard.insert(
        InlineKeyboardButton(text="Назад", callback_data=mission.new(a="back", gid=game_id, mid=0)))
    return keyboard