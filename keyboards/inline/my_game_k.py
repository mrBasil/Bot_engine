
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.db_api import db_game, db_orgs
from aiogram.utils.callback_data import CallbackData


my_game_cd = CallbackData("my_game", "a", "id")
async def get_my_game_keyboard(user_id):
    '''
    a - action
            set    - setting
            create - create
    '''

    # Получаем лимит по играм
    limit_game = await db_orgs.get_limit_game(user_id)

    # Получаем все ID игр
    set_id_game = await db_game.get_all_id(user_id)


    keyboard = InlineKeyboardMarkup(row_width=1)

    if len(set_id_game) > 0:
        for id in set_id_game:

            text_button = await db_game.get_title(id)

            callback =  my_game_cd.new(a="set", id=str(id))

            keyboard.insert(InlineKeyboardButton(text=text_button, callback_data=callback))

    # Проверим не привысил ли орг лимит по играм
    if len(set_id_game) < limit_game:

        callback =  my_game_cd.new(a="create", id=str(user_id))

        keyboard.insert(InlineKeyboardButton(text="Создать игру", callback_data=callback))


    callback = my_game_cd.new(a="back", id=user_id)

    keyboard.insert(InlineKeyboardButton(text="Назад", callback_data=callback))

    return keyboard



setting_cd = CallbackData("setGame", "a", "id")
async def get_setting_game_keyboard(game_id):
    '''
        show - показать игру
        del - удалить игру
        title - сменить название
        desc - сменить описание
        back - назад
        ava - сменить аватар
        type - тип игры индивидуальная или комендная
        dataR - дата релиза
        dataE - дата окончания
        timeE - время конца
        miss - задания
        price - цена за игру
        save - сахранить

        '''
    key = InlineKeyboardMarkup(row_width=2)
    key.insert(InlineKeyboardButton(text="Просмотр игры", callback_data=setting_cd.new(a="show", id=game_id)))
    key.insert(InlineKeyboardButton(text="Название", callback_data=setting_cd.new(a="title", id=game_id)))
    key.insert(InlineKeyboardButton(text="Описание", callback_data=setting_cd.new(a="desc", id=game_id)))
    key.insert(InlineKeyboardButton(text="ПревЬю", callback_data=setting_cd.new(a="ava", id=game_id)))
    key.insert(InlineKeyboardButton(text="Дата выхода", callback_data=setting_cd.new(a="dataR", id=game_id)))
    key.insert(InlineKeyboardButton(text="Дата конца", callback_data=setting_cd.new(a="dataE", id=game_id)))
    key.insert(InlineKeyboardButton(text="Время конца", callback_data=setting_cd.new(a="timeE", id=game_id)))
    key.insert(InlineKeyboardButton(text="Тип игры", callback_data=setting_cd.new(a="type", id=game_id)))
    key.insert(InlineKeyboardButton(text="Цена", callback_data=setting_cd.new(a="price", id=game_id)))
    key.insert(InlineKeyboardButton(text="Задания", callback_data=setting_cd.new(a="miss", id=game_id)))
    key.insert(InlineKeyboardButton(text="Скачать сценарий", callback_data=setting_cd.new(a="save", id=game_id)))
    key.insert(InlineKeyboardButton(text="Удалить", callback_data=setting_cd.new(a="del", id=game_id)))
    key.insert(InlineKeyboardButton(text="Назад", callback_data=setting_cd.new(a="back", id=game_id)))
    return key

async def get_type(game_id):
    '''
    personal
    team
    '''
    key = InlineKeyboardMarkup(row_width=2)
    key.insert(InlineKeyboardButton(text="Персональная", callback_data=setting_cd.new(a="type1", id=game_id)))
    key.insert(InlineKeyboardButton(text="Командная", callback_data=setting_cd.new(a="type2", id=game_id)))
    return key