import logging

from aiogram import types
import io
from aiogram.dispatcher import FSMContext

from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.default import keyboard_cancel

from loader import dp, bot

from keyboards.inline import my_game_k, main_menu_keyboard, mysson_keyboard
from keyboards.inline import mysson_keyboard

from keyboards.inline import code_keyboard

from utils.db_api import db_game, db_orgs, db_mission, db_code
from states.state_mashin import Code


@dp.callback_query_handler(code_keyboard.code_all.filter())
async def all_code_handler(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    mission_id = callback_data.get("mid")
    user_id = call.from_user.id
    game_id = callback_data.get("gid")
    code_id = callback_data.get("cid")
    action = callback_data.get("a")


    if action == "add":
        await call.answer(cache_time=2)
        await db_code.add_new_code(mission_id, game_id)
        title_mission = await db_mission.get_title(mission_id)
        markup = await code_keyboard.all_code_keyboard(mission_id, game_id)
        await call.message.edit_text(f"Коды к Заданию: {title_mission}", reply_markup=markup)

    elif action == "back":
        await call.answer(cache_time=2)
        title_game = await db_game.get_title(game_id)
        title_mission = await db_mission.get_title(mission_id)
        markup = await mysson_keyboard.get_setting_mission(mission_id, game_id)
        text = f"Настройки задания: {title_mission}\nИгра: {title_game}"
        await call.message.edit_text(text=text, reply_markup=markup)

    elif action == "set":
        await call.answer(cache_time=2)
        answer_code = await db_code.get_code(code_id=code_id)
        markup = await code_keyboard.set_codes_keyboard(code_id=code_id)
        text = f"Настройка кода: {answer_code}"
        await call.message.edit_text(text=text, reply_markup=markup)

@dp.callback_query_handler(code_keyboard.code_set.filter())
async def set_code_handler(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")

    user_id = call.from_user.id

    code_id = callback_data.get("cid")
    action = callback_data.get("a")


    if action == "show":
        await call.answer(cache_time=2)

    elif action == "code":
        await call.answer(cache_time=2)


    elif action == "type":
        await call.answer(cache_time=2)

    elif action == "bonus":
        await call.answer(cache_time=2)

    elif action == "comm":
        await call.answer(cache_time=2)

    elif action == "del":
        await call.answer(cache_time=2)

    elif action == "back":
        await call.answer(cache_time=2)
