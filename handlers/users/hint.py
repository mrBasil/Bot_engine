import logging

from aiogram import types
import io
from aiogram.dispatcher import FSMContext

from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.default import keyboard_cancel


from loader import dp

from keyboards.inline import hint_keyboard, mysson_keyboard



from utils.db_api import db_mission, db_hint
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


@dp.callback_query_handler(hint_keyboard.hint_setting_cd.filter())
async def all_hint_handler(call: CallbackQuery, callback_data: dict, state:FSMContext):
    logging.info(f"{callback_data=}")
    hint_id = callback_data.get("hid")
    mission_id = await db_hint.get_mission_id(hint_id)
    game_id = await db_hint.get_game_id(hint_id)
    user_id = call.from_user.id
    action = callback_data.get("a")

    if action == "show":
        await call.answer(cache_time=2)
        title = await db_hint.get_title(hint_id)
        description = await db_hint.get_description(hint_id)
        over_time = await db_hint.get_over_time(hint_id)
        file_id = await db_hint.get_capture_token(hint_id)
        await call.message.edit_text(text=f"Просмотр подсказки: {title}")
        await call.message.answer_photo(file_id, caption=f"Описание: {description}\n")
        markup = await hint_keyboard.get_setting_hint_keyboard(hint_id)
        await call.message.answer(f"Время выхода: через {over_time} мин\n"
                                  f"после начала задания", reply_markup=markup)


    elif action == "title":

        await call.answer(cache_time=2)
        await Hint.Title.set()
        await state.update_data(game_id=game_id, mission_id=mission_id, hint_id=hint_id)
        text = f"Напиши мне новый заголовок! \n"
        markup = keyboard_cancel.keyboard
        await call.message.edit_text(text=text)
        await call.message.answer(text=f"Не больше 100 символов", reply_markup=markup)


    elif action == "des":

        await call.answer(cache_time=2)
        await Hint.Description.set()
        await state.update_data(game_id=game_id, mission_id=mission_id, hint_id=hint_id)
        text = f"Напиши мне новое описание! \n"
        markup = keyboard_cancel.keyboard
        await call.message.edit_text(text=text)
        await call.message.answer(text=f"(не более 4000 символов)", reply_markup=markup)


    elif action == "capt":

        await call.answer(cache_time=2)
        await Hint.Capture.set()
        await state.update_data(game_id=game_id, mission_id=mission_id, hint_id=hint_id)
        text = f"Шли мне Превью задания!"
        markup = keyboard_cancel.keyboard
        await call.message.edit_text(text=text)
        await call.message.answer(text=f"картинку или просто сфоткай", reply_markup=markup)


    elif action == "time":

        await call.answer(cache_time=2)
        await Hint.Over_time.set()
        await state.update_data(game_id=game_id, mission_id=mission_id, hint_id=hint_id)
        text = f"Напиши мне новое время выхода! \n"
        markup = keyboard_cancel.keyboard
        await call.message.edit_text(text=text)
        await call.message.answer(text=f"(не более 4000 символов)", reply_markup=markup)

    elif action == "del":
        await call.answer(cache_time=2)
        await db_hint.del_hint(mission_id)
        markup = await hint_keyboard.get_all_hint_keyboard(mission_id)
        await call.message.edit_text(text="Меню подсказок", reply_markup=markup)

    elif action == "back":
        await call.answer(cache_time=2)
        markup = await hint_keyboard.get_all_hint_keyboard(mission_id)
        await call.message.edit_text(text="Меню подсказок", reply_markup=markup)

@dp.message_handler(state=Hint,content_types=types.ContentTypes.ANY)
async def state_message_all_text(message: types.Message, state: FSMContext):
    state_tr = await state.get_state()
    logging.info(f" content = {message.content_type}, id {message.from_user.id}, state {state_tr}")

    data = await state.get_data()

    hint_id = data.get("hint_id")
    print("hint_id ",hint_id, "state handler hint")

    if message.text == "отмена":
        title_hint = await db_hint.get_title(hint_id)
        markup = await hint_keyboard.get_setting_hint_keyboard(hint_id)
        await state.reset_state(True)
        await message.answer(text="Отменил", reply_markup=ReplyKeyboardRemove())
        text = f"Настройка задания: {title_hint}"
        await message.answer(text=text, reply_markup=markup)
    else:
        if state_tr == Hint.Title.state:
            title = message.text
            await db_hint.set_title(hint_id, title)
            title_hint = await db_hint.get_title(hint_id)
            markup = await hint_keyboard.get_setting_hint_keyboard(hint_id)
            await state.reset_state(True)
            await message.answer(text="Изменил название", reply_markup=ReplyKeyboardRemove())
            text = f"Настройка подсказки: {title_hint}"
            await message.answer(text=text, reply_markup=markup)

        elif state_tr == Hint.Description.state:
            description = message.text
            await db_hint.set_description(hint_id, description)
            title_des = await db_hint.get_title(hint_id)
            markup = await hint_keyboard.get_setting_hint_keyboard(hint_id)
            await state.reset_state(True)
            await message.answer(text="Изменил описание", reply_markup=ReplyKeyboardRemove())
            text = f"Настройка подсказки: {title_des}"
            await message.answer(text=text, reply_markup=markup)

        elif state_tr == Hint.Over_time.state:
            over_time = message.text
            if await db_hint.set_over_time(hint_id, over_time):
                title_des = await db_hint.get_title(hint_id)
                markup = await hint_keyboard.get_setting_hint_keyboard(hint_id)
                await state.reset_state(True)
                await message.answer(text="Изменил время", reply_markup=ReplyKeyboardRemove())
                text = f"Настройка подсказки: {title_des}"
                await message.answer(text=text, reply_markup=markup)
            else:
                await message.answer(text="Что-то не так, попробуй еще раз")

        elif state_tr == Hint.Capture.state:

            title_hint = await db_hint.get_title(hint_id)

            ph = await message.photo[-1].get_file()
            token_photo = message.photo[-1].file_id
            file = io.BytesIO()
            await ph.download(destination=file)
            await db_hint.set_capture(hint_id, file)
            await db_hint.set_capture_token(hint_id, token_photo)
            await message.answer(text="Изменил превью подсказки", reply_markup=ReplyKeyboardRemove())
            text = f"Настройки подсказки: {title_hint}"
            markup = await hint_keyboard.get_setting_hint_keyboard(hint_id)
            await state.reset_state(True)
            await message.answer(text=text, reply_markup=markup)