import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp, bot

from keyboards.inline import my_profile_k
from keyboards.inline.main_menu_keyboard import getMenu

from utils.db_api import db_orgs
from states.state_mashin import Profile

@dp.callback_query_handler(text_contains="my_profile")
async def my_profile_settings(call: CallbackQuery):
    user_id = call.from_user.id
    await call.answer(cache_time=1)
    markup = my_profile_k.get_my_profil_settings(user_id)
    await call.message.edit_text(text="Профиль", reply_markup=markup)

@dp.callback_query_handler(my_profile_k.menu_profile.filter())
async def profile_set_handler(call: CallbackQuery, callback_data: dict, state:FSMContext):
    '''
        show
        login
        pass
        name
        family
        city
        team
        back
        '''

    user_id = call.from_user.id
    logging.info(f"{callback_data=}")

    action = callback_data.get("a")
    if action == "back":
        markup = await getMenu()
        await call.message.edit_text(text="Вот тебе меню оно все может!", reply_markup=markup)

    elif action == "show":
        print("show profile")
        await call.answer()
        log_in = await db_orgs.get_login(user_id)
        password =  await db_orgs.get_pas(user_id)
        name = await db_orgs.get_first_name(user_id)
        family = await db_orgs.get_last_name(user_id)
        city = await db_orgs.get_city(user_id)
        markup = my_profile_k.get_my_profil_settings(user_id)

        text = (f"LOG_IN: {log_in}\n"
               f"PASSWORD: {password}\n"
                f"Имя: {name}\n"
                f"Фамилия: {family}\n"
                f"Location: {city}")

        await call.message.edit_text(text=text, reply_markup=markup)

    elif action == "login":
        await Profile.LogIn.set()
        await state.update_data(user_id=user_id)
        text = f" Шли мне новый Log_in! \n(не более 50 символов)"
        await call.message.edit_text(text=text)

    elif action == "pass":
        await Profile.Password.set()
        await state.update_data(user_id=user_id)
        text = f" Шли мне новый PASSWORD! \n(не более 50 символов)"
        await call.message.edit_text(text=text)

    elif action == "name":
        await Profile.FirstName.set()
        await state.update_data(user_id=user_id)
        text = f" Шли мне свое Имя! \n(не более 20 символов)"
        await call.message.edit_text(text=text)

    elif action == "family":
        await Profile.LastName.set()
        await state.update_data(user_id=user_id)
        text = f" Шли мне свою Фамилию! \n(не более 20 символов)"
        await call.message.edit_text(text=text)

    elif action == "city":
        await Profile.CITY.set()
        await state.update_data(user_id=user_id)
        text = f" Шли мне свою Локацию! \n(не более 50 символов)"
        await call.message.edit_text(text=text)

    elif action == "team":
        print("team profile")
        await call.answer()
        markup = my_profile_k.get_my_profil_settings(user_id)
        await call.message.edit_text(text="В разработке", reply_markup=markup )

@dp.message_handler(state=Profile, content_types=["text"])
async def state_message_all_text(message: types.Message, state: FSMContext):

    state_tr = await state.get_state()

    logging.info(f" content = {message.content_type}, id {message.from_user.id}, state {state_tr}")
    user_id = message.from_user.id
    if state_tr == Profile.LogIn.state:
        # Обновляем логин профиля
        markup =  my_profile_k.get_my_profil_settings(user_id)
        login = message.text
        await db_orgs.set_login(user_id,login )
        text = f"Обновил LOG_IN: {login}"
        await state.reset_state(True)
        await message.answer(text=text, reply_markup=markup)

    elif state_tr == Profile.Password.state:
        # Обновляем Password профиля
        markup = my_profile_k.get_my_profil_settings(user_id)
        password= message.text
        await db_orgs.set_pas(user_id, password)
        text = f"Обновил Password: {password}"
        await state.reset_state(True)
        await message.answer(text=text, reply_markup=markup)

    elif state_tr == Profile.FirstName.state:
        # Обновляем имя профиля
        markup = my_profile_k.get_my_profil_settings(user_id)
        name = message.text
        await db_orgs.set_first_name(user_id, name)
        text = f"Обновил Имя: {name}"
        await state.reset_state(True)
        await message.answer(text=text, reply_markup=markup)

    elif state_tr == Profile.LastName.state:
        # Обновляем Фамилию профиля
        markup = my_profile_k.get_my_profil_settings(user_id)
        family = message.text
        await db_orgs.set_last_name(user_id, family)
        text = f"Обновил фамилию: {family}"
        await state.reset_state(True)
        await message.answer(text=text, reply_markup=markup)

    elif state_tr == Profile.CITY.state:
        # Обновляем локацию профиля
        markup = my_profile_k.get_my_profil_settings(user_id)
        location = message.text
        await db_orgs.set_city(user_id, location)
        text = f"Обновил локацю: {location}"
        await state.reset_state(True)
        await message.answer(text=text, reply_markup=markup)

    else:
        markup = await main_menu_keyboard.getMenu()
        await state.reset_state(True)
        await message.answer(
            text=f"Я пытался, но не понял, что ты от меня хочешь? \nПопробуй найти ответ сам, в меню!",
            reply_markup=markup
        )
