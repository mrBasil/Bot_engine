from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.main_menu_keyboard import getMenu
from utils.db_api import db_orgs


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    if await db_orgs.add_new_org(user_id):
        markup = await getMenu()
        await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=markup)
