
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.db_api import db_game, db_orgs, db_mission
from aiogram.utils.callback_data import CallbackData

mission = CallbackData("miss", "gid", "mid")
mission_add = CallbackData("mission", "a", "gid")
'''
gid -  game_id
mid -  mission_id
'''
async def get_all_mission(game_id):

    id = await db_mission.get_all_id(game_id)

    key = InlineKeyboardMarkup(row_width=2)
    if len(id)>0:
        for i in id:
            title = await db_mission.get_title(i)
            key.insert(InlineKeyboardButton(text=title, callback_data=mission.new(gid=game_id, mid=i)))
    key.insert(InlineKeyboardButton(text="Добавить", callback_data=mission_add.new(a="add", gid="game_id")))
    key.insert(InlineKeyboardButton(text="Назад", callback_data=mission_add.new(a="back", gid="game_id")))
    return key


