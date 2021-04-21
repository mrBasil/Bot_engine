

import logging

from aiogram import types
import io
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, InlineQueryResult

from keyboards.default import keyboard_cancel


from loader import dp, bot

from keyboards.inline import my_game_k, main_menu_keyboard, mysson_keyboard
from keyboards.inline import mysson_keyboard
from keyboards.inline import code_keyboard

from utils.db_api import db_game, db_orgs, db_mission, db_code
from states.state_mashin import Game_state, Mission



import datetime

@dp.inline_handler()
async def all_mission_handler(query: types.InlineQuery):
    invite = query.query
    if invite == "invite":
        await query.answer(results=[InlineQueryResult()],switch_pm_text="Text")