import logging

from aiogram import types
import io
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.default import keyboard_cancel


from loader import dp, bot

from keyboards.inline import hint_keyboard, mysson_keyboard



from utils.db_api import db_game, db_orgs, db_mission, db_code, db_hint
from states.state_mashin import Hint

@dp.callback_query_handler(hint_keyboard.hint_all_cd.filter())
async def all_hint_handler(call: CallbackQuery, callback_data: dict, state:FSMContext):

    logging.info(f"{callback_data=}")
    hint_id = callback_data.get("hid")
    mission_id = callback_data.get("mid")
    game_id = await db_mission.get_game_id(mission_id)
    user_id = call.from_user.id
    action = callback_data.get("a")
    # print(mission_id, "handler hint")

    if action == "add":
        await call.answer(cache_time=2)
        await db_hint.add_hint(mission_id=mission_id, game_id=game_id)
        title_mission = await db_mission.get_title(mission_id)
        markup = await hint_keyboard.get_all_hint_keyboard(mission_id)
        await call.message.edit_text(f"Задания к игре: {title_mission}", reply_markup=markup)

    elif action == "back":
        await call.answer(cache_time=2)
        title_mission = await db_mission.get_title(mission_id)

        text_message = f"Настройка задания {title_mission}"
        markup = await mysson_keyboard.get_setting_mission(mission_id, game_id)
        await call.message.edit_text(text=text_message, reply_markup=markup)

    elif action == "set":
        await call.answer(cache_time=2)
        title_hint = await db_hint.get_title(hint_id)
        markup = await hint_keyboard.get_setting_hint_keyboard(hint_id)
        text = f"Настройка подсказки: {title_hint}"
        await call.message.edit_text(text=text, reply_markup=markup)