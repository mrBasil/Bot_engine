import logging

from aiogram import types
import io
from aiogram.dispatcher import FSMContext

from aiogram.types import  CallbackQuery, ReplyKeyboardRemove

from keyboards.default import keyboard_cancel


from loader import dp

from keyboards.inline import my_game_k, hint_keyboard
from keyboards.inline import mysson_keyboard
from keyboards.inline import code_keyboard

from utils.db_api import db_game,  db_mission, db_code, db_hint
from states.state_mashin import Mission

@dp.callback_query_handler(mysson_keyboard.mission_add.filter())
async def all_mission_handler(call: CallbackQuery, callback_data: dict, state:FSMContext):
    logging.info(f"{callback_data=}")
    game_id = callback_data.get("gid")
    user_id = call.from_user.id
    action = callback_data.get("a")
    mission_id = callback_data.get("mid")

    if action == "add":
        await call.answer(cache_time=2)
        await db_mission.add_mission(user_id, game_id)
        title_game = await db_game.get_title(game_id)
        markup = await mysson_keyboard.get_all_mission(game_id)
        await call.message.edit_text(f"Задания к игре: {title_game}", reply_markup=markup)

    elif action == "back":
        await call.answer(cache_time=2)
        title_game = await db_game.get_title(game_id)
        text_message = f"Настройка игры {title_game}"
        markup = await my_game_k.get_setting_game_keyboard(game_id)
        await call.message.edit_text(text=text_message, reply_markup=markup)

    elif action == "set":
        await call.answer(cache_time=2)
        title_mis = await db_mission.get_title(mission_id)
        markup = await mysson_keyboard.get_setting_mission(mission_id, game_id)
        text = f"Настройка задания: {title_mis}"
        await call.message.edit_text(text=text, reply_markup=markup)

@dp.callback_query_handler(mysson_keyboard.mission.filter())
async def settings_mission_handler(call: CallbackQuery, callback_data: dict, state:FSMContext):
    logging.info(f"{callback_data=}")
    game_id = callback_data.get("gid")
    mission_id = callback_data.get("mid")
    user_id = call.from_user.id
    action = callback_data.get("a")

    if action=="show":
        await call.answer(cache_time=2)
        title = await db_mission.get_title(mission_id)
        description = await db_mission.get_description(mission_id)
        number = await db_mission.get_number(mission_id)
        over_time = await db_mission.get_over_time(mission_id)
        file_id = await db_mission.get_capture_token(mission_id)
        len_cod = len( await db_code.get_all_id(mission_id))
        len_hint = len(await db_hint.get_all_id(mission_id))

        await call.message.edit_text(text=f"Просмотр Задания: {title}")
        await call.message.answer_photo(file_id, caption=f"Описание: {description}\n")
        markup = await mysson_keyboard.get_setting_mission(mission_id, game_id)
        await call.message.answer(f"Подсказок: {len_hint}\n"
                                  f"Количество кодов : {len_cod}\n"
                                  f"Автослив: {over_time} мин\n"
                                  f"Номер по порядку: {number}\n", reply_markup=markup)

    elif action == "title":
        await call.answer(cache_time=2)
        await Mission.Title.set()
        await state.update_data(game_id=game_id, mission_id=mission_id)
        text = f"Напиши мне новый заголовок! \n"
        markup = keyboard_cancel.keyboard
        await call.message.edit_text(text=text)
        await call.message.answer(text=f"Не больше 100 символов", reply_markup = markup)


    elif action == "des":
        await call.answer(cache_time=2)
        await Mission.Description.set()
        await state.update_data(game_id=game_id, mission_id=mission_id)
        text = f"Напиши мне новое описание! \n"
        markup = keyboard_cancel.keyboard
        await call.message.edit_text(text=text)
        await call.message.answer(text=f"(не более 4000 символов)", reply_markup=markup)

    elif action == "capt":
        await call.answer(cache_time=2)
        await Mission.Capture.set()
        await state.update_data(game_id=game_id, mission_id=mission_id)
        text = f"Шли мне Превью задания!"
        markup = keyboard_cancel.keyboard
        await call.message.edit_text(text=text)
        await call.message.answer(text=f"картинку или просто сфоткай", reply_markup=markup)

    elif action == "del":
        await call.answer(cache_time=2)
        await db_mission.del_mission(mission_id)
        markup = await mysson_keyboard.get_all_mission(game_id)
        await call.message.edit_text(text="Меню заданий", reply_markup=markup)

    elif action == "num":
        await call.answer(cache_time=2)
        await Mission.Number.set()
        await state.update_data(game_id=game_id, mission_id=mission_id)
        text = f"Напиши мне порядковый номер задания в игре! \n"
        markup = keyboard_cancel.keyboard
        await call.message.edit_text(text=text)
        await call.message.answer(text=f"(Пожалуйста, только цифры!)", reply_markup=markup)

    elif action == "time":
        await call.answer(cache_time=2)
        await Mission.Over_time.set()
        await state.update_data(game_id=game_id, mission_id=mission_id)
        text = f"Время длительности задания в минутах! \n"
        markup = keyboard_cancel.keyboard
        await call.message.edit_text(text=text)
        await call.message.answer(text=f"(Пожалуйста, только цифры!)", reply_markup=markup)

    elif action == "code":
        await call.answer(cache_time=2)
        title = await db_mission.get_title(mission_id)
        text = f"Меню кодов задания: {title}"
        markup = await code_keyboard.all_code_keyboard(mission_id, game_id)
        await call.message.edit_text(text=text, reply_markup=markup)

    elif action == "hint":
        await call.answer(cache_time=2)
        title = await db_mission.get_title(mission_id)
        text = f"Меню подсказок задания: {title}"
        markup = await hint_keyboard.get_all_hint_keyboard(mission_id)
        await call.message.edit_text(text=text, reply_markup=markup)

    elif action =="back":
        await call.answer(cache_time=2)
        markup = await mysson_keyboard.get_all_mission(game_id)
        await call.message.edit_text(text="Задания", reply_markup=markup)



@dp.message_handler(state=Mission,content_types=types.ContentTypes.ANY)
async def state_message_all_text(message: types.Message, state: FSMContext):
    state_tr = await state.get_state()
    logging.info(f" content = {message.content_type}, id {message.from_user.id}, state {state_tr}")
    user_id = message.from_user.id
    data = await state.get_data()
    game_id = data.get("game_id")
    mission_id = data.get("mission_id")

    if message.text == "отмена":
        title_mis = await db_mission.get_title(mission_id)
        markup = await mysson_keyboard.get_setting_mission(mission_id, game_id)
        await state.reset_state(True)
        await message.answer(text="Отменил", reply_markup=ReplyKeyboardRemove())
        text = f"Настройка задания: {title_mis}"
        await message.answer(text=text, reply_markup=markup)
    else:
        if state_tr == Mission.Title.state:
            title = message.text
            await db_mission.set_title(mission_id, title )
            title_mis = await db_mission.get_title(mission_id)
            markup = await mysson_keyboard.get_setting_mission(mission_id, game_id)
            await state.reset_state(True)
            await message.answer(text="Изменил название", reply_markup=ReplyKeyboardRemove())
            text = f"Настройка задания: {title_mis}"
            await message.answer(text=text, reply_markup=markup)

        elif state_tr == Mission.Description.state:
            description = message.text
            await db_mission.set_description(mission_id, description )
            title_mis = await db_mission.get_title(mission_id)
            markup = await mysson_keyboard.get_setting_mission(mission_id, game_id)
            await state.reset_state(True)
            await message.answer(text="Изменил описание", reply_markup=ReplyKeyboardRemove())
            text = f"Настройка задания: {title_mis}"
            await message.answer(text=text, reply_markup=markup)

        elif state_tr == Mission.Capture.state:
            print("capture state mission")
            title_mis = await db_mission.get_title(mission_id)

            ph = await message.photo[-1].get_file()
            token_photo = message.photo[-1].file_id
            file = io.BytesIO()
            await ph.download(destination=file)
            await db_mission.set_capture(mission_id, file)
            await db_mission.set_capture_token(mission_id, token_photo)
            await message.answer(text="Изменил превью задания", reply_markup=ReplyKeyboardRemove())
            text = f"Обновил превью в задании: {title_mis}"
            markup = await mysson_keyboard.get_setting_mission(mission_id, game_id)
            await state.reset_state(True)
            await message.answer(text=text, reply_markup=markup)

        elif state_tr == Mission.Over_time.state:
            time = message.text
            await db_mission.set_over_time(mission_id, time)
            title_mis = await db_mission.get_title(mission_id)
            markup = await mysson_keyboard.get_setting_mission(mission_id, game_id)
            await state.reset_state(True)
            await message.answer(text="Именил время автоперехода", reply_markup=ReplyKeyboardRemove())
            text = f"Обновил время автоперехода : {title_mis}"
            await message.answer(text=text, reply_markup=markup)

        elif state_tr == Mission.Number.state:
            number = message.text
            await db_mission.set_number(mission_id, number )
            title_mis = await db_mission.get_title(mission_id)
            markup = await mysson_keyboard.get_setting_mission(mission_id, game_id)
            await state.reset_state(True)
            await message.answer(text="Изменил номер по порядку", reply_markup=ReplyKeyboardRemove())
            text = f"Обновил порядковый номер задания: {title_mis}"
            await message.answer(text=text, reply_markup=markup)
