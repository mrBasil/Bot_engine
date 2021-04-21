

import logging

from aiogram import types
import io
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, InlineQueryResult, InlineKeyboardMarkup, \
    InlineKeyboardButton, InputMessageContent, InlineQueryResultArticle, InlineQueryResultPhoto
from aiogram.utils.callback_data import CallbackData

from keyboards.default import keyboard_cancel


from loader import dp, bot

from keyboards.inline import my_game_k, main_menu_keyboard, mysson_keyboard
from keyboards.inline import mysson_keyboard
from keyboards.inline import code_keyboard

from utils.db_api import db_game, db_orgs, db_mission, db_code
from states.state_mashin import Game_state, Mission

keyboard = InlineKeyboardMarkup()
invite  = CallbackData("invite", "gid")

keyboard.add(InlineKeyboardButton(text="Стать оргом", callback_data= invite.new(gid="2")))
game= "Игра всех времен"
mess = InputMessageContent(message_text=f"Стань оргом в игре: {game}")
atikl = InlineQueryResultArticle(id="1", title="Пригласить орга", input_message_content=mess, reply_markup=keyboard)
r =[]
r.append(atikl)

import datetime


@dp.inline_handler()
async def all_mission_handler(query: types.InlineQuery):
    invite = query.query
    if invite == "invite":
        await query.answer(results=r)

@dp.callback_query_handler(invite.filter())
async def settings_mission_handler(call: CallbackQuery, callback_data: dict, state:FSMContext):
    await call.answer("Не сегодня")