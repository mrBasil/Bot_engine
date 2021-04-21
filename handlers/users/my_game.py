import logging

from aiogram import types
import io
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.default import keyboard_cancel
from keyboards.inline.main_menu_keyboard import getMenu

from loader import dp, bot

from keyboards.inline import my_game_k, main_menu_keyboard, mysson_keyboard
from utils.db_api import db_game, db_orgs, db_mission
from states.state_mashin import Game_state

import datetime

@dp.callback_query_handler(text_contains="my_games")
async def my_games(call: CallbackQuery):

    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.answer(cache_time=1)
    markup = await my_game_k.get_my_game_keyboard(call.from_user.id)
    await call.message.edit_text(text="Меню игр", reply_markup=markup)

@dp.callback_query_handler(my_game_k.my_game_cd.filter())
async def chousen_game_handler(call: CallbackQuery, callback_data: dict):

    id = call.from_user.id
    logging.info(f"{callback_data=}")

    action = callback_data.get("a")
    if action == "back":
        await call.answer(cache_time=2)
        markup = await getMenu()
        await call.message.edit_text(text="Вот тебе меню оно все может!", reply_markup=markup)

    elif action == "create":
        await call.answer(cache_time=2)
        await db_game.add_new_game(id)
        markup = await my_game_k.get_my_game_keyboard(id)
        await call.message.edit_text(text="Меню игр", reply_markup=markup)

    elif action == "set":
        await call.answer(cache_time=2)
        game_id = callback_data.get("id")
        title_game = await db_game.get_title(game_id)
        text_message = f"Настройка игры {title_game}"
        markup = await my_game_k.get_setting_game_keyboard(game_id)
        await call.message.edit_text(text=text_message, reply_markup=markup)

@dp.callback_query_handler(my_game_k.setting_cd.filter())
async def settings_game_handler(call: CallbackQuery, callback_data: dict, state:FSMContext):

    user_id = call.from_user.id
    logging.info(f"{callback_data=}")

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
                save - скачать

                '''
    action = callback_data.get("a")
    game_id = callback_data.get("id")

    if action=="show":
        print("show")
        await call.answer(cache_time=2)
        title = await db_game.get_title(game_id)
        description = await db_game.get_description(game_id)
        len_mission = len(await db_mission.get_all_id(game_id))
        dataR = await db_game.get_dataRelise(game_id)
        dataE = await db_game.get_dataEnd(game_id)
        type_ = await db_game.get_type(game_id)
        price = await db_game.get_price(game_id)
        file_id = await db_game.get_capture_token(game_id)
        await call.message.edit_text(text=f"Просмотр игры: {title}")
        await call.message.answer_photo(file_id)
        markup = await my_game_k.get_setting_game_keyboard(game_id)
        await call.message.answer(f"Описание: {description}\n"
                                  f"Заданий: {len_mission}\n"
                                     f"Дата выхода: {dataR}\n"
                                     f"Дата окончания: {dataE}\n"
                                     f"Тип игры: {type_}\n"
                                     f"Цена игры: {price}", reply_markup=markup)

    elif action=="del":
        await db_game.del_game(game_id)
        await call.answer(cache_time=2)

        markup = await my_game_k.get_my_game_keyboard(user_id)
        await call.message.edit_text(text="Меню игр", reply_markup=markup)


    elif action=="title":
        await call.answer(cache_time=2)
        await Game_state.Title.set()
        await state.update_data(game_id=game_id)
        text = f" Шли мне новое Название игры! \n"
        await call.message.edit_text(text=text)
        markup = keyboard_cancel.keyboard
        await call.message.answer(text="(не более 100 символов)", reply_markup=markup)

    elif action=="desc":
        print("desc")
        await call.answer(cache_time=2)
        await Game_state.Description.set()
        await state.update_data(game_id=game_id)
        text = f" Шли мне новое Описание игры! \n"
        await call.message.edit_text(text=text)
        markup = keyboard_cancel.keyboard
        await call.message.answer(text="(Не более 4000 символов)", reply_markup=markup)

    elif action=="back":
        await call.answer(cache_time=2)
        markup = await my_game_k.get_my_game_keyboard(user_id)
        await call.message.edit_text(text="Меню игр", reply_markup=markup)

    elif action == "ava":
        print("ava ")
        await call.answer(cache_time=2)
        await Game_state.Capture.set()
        await state.update_data(game_id=game_id)
        text = f" Шли мне новую превью к игре!"
        await call.message.edit_text(text=text)
        markup = keyboard_cancel.keyboard
        await call.message.answer(text="(Можешь просто фотку)", reply_markup=markup)


    elif action == "type":
        print("type")
        await call.answer(cache_time=2)
        markup = await my_game_k.get_type(game_id)
        await call.message.edit_text(text="Выбери тип игры", reply_markup=markup)
    elif action == "type1":
        print("type1")
        await call.answer(cache_time=2)
        await db_game.set_type(game_id, 1)
        markup = await my_game_k.get_setting_game_keyboard(game_id)
        await call.message.edit_text(text="Обновил тип игры", reply_markup=markup)
    elif action == "type2":
        print("type2")
        await call.answer(cache_time=2)
        await db_game.set_type(game_id, 0)
        markup = await my_game_k.get_setting_game_keyboard(game_id)
        await call.message.edit_text(text="Обновил тип игры тип игры", reply_markup=markup)

    elif action == "dataR":
        print("dataR")
        await call.answer(cache_time=2)
        await Game_state.Data_relise.set()
        await state.update_data(game_id=game_id)
        text = f" Пришли мне дату, когда ты планируешь провести игру!\n "
        await call.message.edit_text(text=text)
        markup = keyboard_cancel.keyboard
        await call.message.answer(text="(Формата: гггг-мм-дд)", reply_markup=markup)


    elif action == "dataE":
        print("dataE ")
        await call.answer(cache_time=2)
        await Game_state.Data_end.set()
        await state.update_data(game_id=game_id)
        text = f" Пришли мне дату, когда ты планируешь закончить игру!\n Формата: гггг-мм-дд"
        await call.message.edit_text(text=text)
        markup = keyboard_cancel.keyboard
        await call.message.answer(text="(Формата: гггг-мм-дд)", reply_markup=markup)


    elif action == "timeE":
        print("timeE")
        await call.answer(cache_time=2)
        await Game_state.Time_end.set()
        await state.update_data(game_id=game_id)
        text = f" Пришли мне время, во сколько ты планируешь закончить игру!\n"
        await call.message.edit_text(text=text)
        markup = keyboard_cancel.keyboard
        await call.message.answer(text="(Формата: чч-mm)", reply_markup=markup)


    elif action == "miss":
        print("miss")
        await call.answer(cache_time=2)
        title_game = await db_game.get_title(game_id)
        markup = await mysson_keyboard.get_all_mission(game_id)
        await call.message.edit_text(f"Задания к игре: {title_game}", reply_markup=markup)

    elif action == "price":
        print("price")
        await call.answer(cache_time=2)
        await Game_state.Price.set()
        await state.update_data(game_id=game_id)
        text = f"Пришли мне цену которую ты планируешь брать с игроков\n"
        await call.message.edit_text(text=text)
        markup = keyboard_cancel.keyboard
        await call.message.answer(text="( Пожалуйста, только цифры)", reply_markup=markup)

    elif action == "save":
        await call.answer(cache_time=2)
        text = f"Настройки игры"
        await call.message.edit_text(text=text)
        markup = await my_game_k.get_setting_game_keyboard(game_id)
        await call.message.edit_text(text="Тут будет файл со сценарием как только доделаю")
        await call.message.answer(text=text, reply_markup=markup)

@dp.message_handler(state=Game_state.Capture.state, content_types=["photo"])
async def state_message_all_photo(message: types.Message, state: FSMContext):

    state_ = Game_state.Capture.state
    state_tr = await state.get_state()

    logging.info(f" content = {message.content_type}, id {message.from_user.id}, state {state_tr}")

    user_id = message.from_user.id

    data = await state.get_data()
    game_id = data.get("game_id")

    print(f"{game_id} , {user_id}")


    if state_tr == state_:

        markup = await my_game_k.get_setting_game_keyboard(game_id)

        ph = await message.photo[-1].get_file()
        token_photo = message.photo[-1].file_id
        file = io.BytesIO()
        await ph.download(destination=file)
        await db_game.set_capture(game_id, file)
        await db_game.set_capture_token(game_id, token_photo)
        title_game = await db_game.get_title(game_id)
        text = f"Обновил превью в игре: {title_game}"
        await state.reset_state(True)
        await message.answer(text=text, reply_markup=markup)

    else:
        markup = await main_menu_keyboard.getMenu()
        await state.reset_state(True)
        await message.answer(
            text=f"Я пытался, но не понял, что ты от меня хочешь? \nПопробуй найти ответ сам, в меню!",
            reply_markup=markup
        )

@dp.message_handler(state=Game_state, content_types=["text"])
async def state_message_all_text(message: types.Message, state: FSMContext):

    state_tr = await state.get_state()

    logging.info(f" content = {message.content_type}, id {message.from_user.id}, state {state_tr}")

    user_id = message.from_user.id

    data = await state.get_data()
    game_id = data.get("game_id")

    print(f"{game_id} , {user_id} texts handler")
    if message.text == "отмена":
        await state.reset_state(True)
        await message.answer(text="Отменил", reply_markup=ReplyKeyboardRemove())
        title_game = await db_game.get_title(game_id)
        text_message = f"Настройка игры {title_game}"
        markup = await my_game_k.get_setting_game_keyboard(game_id)
        await message.answer(text=text_message, reply_markup=markup)
    else:


        if state_tr == Game_state.Title.state:
            # Обновляем тайтл в игре
            markup = await my_game_k.get_setting_game_keyboard(game_id)
            title_game = message.text
            await db_game.set_title(game_id, title_game)
            await message.answer(text="Обновил название", reply_markup=ReplyKeyboardRemove())
            text = f"Настройка игры: {title_game}"
            await state.reset_state(True)
            await message.answer(text=text, reply_markup=markup)

        elif state_tr == Game_state.Description.state:
            # Обновляем описание в игре
            markup = await my_game_k.get_setting_game_keyboard(game_id)
            description = message.text
            title_game = await db_game.get_title(game_id)
            await db_game.set_description(game_id, description)
            await message.answer(text="Обновил описание", reply_markup=ReplyKeyboardRemove())
            text = f"Настройки игры: {title_game}"
            await state.reset_state(True)
            await message.answer(text=text, reply_markup=markup)

        elif state_tr == Game_state.Data_relise.state:
            # Обновляем дату выхода
            markup = await my_game_k.get_setting_game_keyboard(game_id)
            data_r = message.text
            title_game = await db_game.get_title(game_id)

            if await db_game.set_dataRelise(game_id, data_r):
                await message.answer(text="Обновил дату выхода", reply_markup=ReplyKeyboardRemove())
                text = f"Настройки игры: {title_game}"
                await state.reset_state(True)
                await message.answer(text=text, reply_markup=markup)
            else:
                data_tuday = datetime.date.today()
                await message.answer(text=f"Ты уверен что ввел все правильно?\n"
                                          f"Должно было получиться как-то так: {data_tuday}\n"
                                          f"Попробуй еще раз")

        elif state_tr == Game_state.Data_end.state:
            # Обновляем дату окончания
            markup = await my_game_k.get_setting_game_keyboard(game_id)
            data_e = message.text
            title_game = await db_game.get_title(game_id)

            if await db_game.set_dataEnd(game_id, data_e):
                await message.answer(text="Обновил дату окончания", reply_markup=ReplyKeyboardRemove())
                text = f"Настройки игры: {title_game}"
                await state.reset_state(True)
                await message.answer(text=text, reply_markup=markup)
            else:
                data_tuday = datetime.date.today()
                await message.answer(text=f"Ты уверен что ввел все правильно?\n"
                                          f"Должно было получиться как-то так: {data_tuday}\n"
                                          f"Попробуй еще раз")

        elif state_tr == Game_state.Time_end.state:
            # Обновляем время окончания
            markup = await my_game_k.get_setting_game_keyboard(game_id)
            time_e = message.text
            title_game = await db_game.get_title(game_id)

            if await db_game.set_timeEnd(game_id, time_e):
                await message.answer(text="Обновил время окончания", reply_markup=ReplyKeyboardRemove())
                text = f"Настройки игры: {title_game}"
                await state.reset_state(True)
                await message.answer(text=text, reply_markup=markup)
            else:
                data_tuday = datetime.time
                await message.answer(text=f"Ты уверен что ввел все правильно?\n"
                                          f"Должно было получиться как-то так: {data_tuday}\n"
                                          f"Попробуй еще раз")

        elif state_tr == Game_state.Price.state:
            # Обновляем цену игры
            markup = await my_game_k.get_setting_game_keyboard(game_id)
            price = message.text
            title_game = await db_game.get_title(game_id)

            if await db_game.set_price(game_id, price):
                await message.answer(text="Обновил цену игры", reply_markup=ReplyKeyboardRemove())
                text = f"Настройки игры: {title_game}"
                await state.reset_state(True)
                await message.answer(text=text, reply_markup=markup)
            else:
                data_tuday = datetime.time
                await message.answer(text=f"Ты уверен что ввел все правильно?\n"
                                          f"Должно получиться как-то так: 200.5\n"
                                          f"Попробуй еще раз")

        else:
            markup = await main_menu_keyboard.getMenu()
            await state.reset_state(True)
            await message.answer(
                text=f"Я пытался, но не понял, что ты от меня хочешь? \nПопробуй найти ответ сам, в меню!",
                reply_markup=markup
            )