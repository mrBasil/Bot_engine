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
async def all_code_handler(call: CallbackQuery, callback_data: dict, state:FSMContext):
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
async def set_code_handler(call: CallbackQuery, callback_data: dict,state:FSMContext):

    logging.info(f"{callback_data=}")
    user_id = call.from_user.id
    code_id = callback_data.get("cid")
    action = callback_data.get("a")
    game_id = await db_code.get_game_id(code_id)
    mission_id = await db_code.get_mission_id(code_id)

    if action == "show":
        await call.answer(cache_time=2)
        code = await db_code.get_code(code_id)
        code_type = await db_code.get_type(code_id)
        comment = await db_code.get_comment(code_id)
        if code_type == "checkpoint":
            text = f"Код: {code}\n" \
                   f"Тип кода: Проходной\n" \
                   f"Комментарий: {comment}"
        else:
            time_bonus = await db_code.get_bonus_time(code_id)
            text = f"Код: {code}\n Тип кода: Бонусный\n" \
                   f"Бонусное время: {time_bonus}\n" \
                   f"Комментарий: {comment}"

        markup = await code_keyboard.set_codes_keyboard(code_id)
        await call.message.edit_text(text=text, reply_markup=markup)

    elif action == "code":
        await call.answer(cache_time=2)
        await Code.Code_.set()
        await state.update_data(game_id=game_id, mission_id=mission_id, code_id=code_id)
        text = f"Напиши мне новое значение кода\n"
        await call.message.edit_text(text=text)
        markup = keyboard_cancel.keyboard
        await call.message.answer(text="(Не более 20 символов)", reply_markup=markup)


    elif action == "type":
        await call.answer(cache_time=2)

        text = f"Выбери тип кода\n"
        await call.message.edit_text(text=text)
        markup = await code_keyboard.set_type_code(code_id)
        await call.message.edit_text(text=text, reply_markup=markup)

    elif action == "type1":
        await call.answer(cache_time=2)
        await db_code.set_type(code_id, "checkpoint")
        code = await db_code.get_code(code_id)
        text = f"Настройка кода: {code}\n"
        markup = await code_keyboard.set_codes_keyboard(code_id)
        await call.message.edit_text(text=text, reply_markup=markup)

    elif action == "type2":
        await call.answer(cache_time=2)
        await db_code.set_type(code_id, "bonus")
        code = await db_code.get_code(code_id)
        text = f"Настройка кода: {code}\n"
        markup = await code_keyboard.set_codes_keyboard(code_id)
        await call.message.edit_text(text=text, reply_markup=markup)


    elif action == "bonus":
        await call.answer(cache_time=2)
        await Code.BonusTime.set()
        await state.update_data(game_id=game_id, mission_id=mission_id, code_id=code_id)
        text = f"Напиши мне бонусное время в минутах\n"
        await call.message.edit_text(text=text)
        markup = keyboard_cancel.keyboard
        await call.message.answer(text="(Только цифры)", reply_markup=markup)

    elif action == "comm":
        await call.answer(cache_time=2)
        await Code.Comment.set()
        await state.update_data(game_id=game_id, mission_id=mission_id, code_id=code_id)
        text = f"Напиши комментарий к коду\n"
        await call.message.edit_text(text=text)
        markup = keyboard_cancel.keyboard
        await call.message.answer(text="(Не больше 50 символов)", reply_markup=markup)

    elif action == "del":
        await call.answer(cache_time=2)
        await db_code.del_code(code_id)

        text = f"Настройки кодов"
        markup = await code_keyboard.all_code_keyboard(mission_id, game_id)
        await call.message.edit_text(text=text, reply_markup=markup)

    elif action == "back":
        await call.answer(cache_time=2)
        text = f"Настройки кодов"
        markup = await code_keyboard.all_code_keyboard(mission_id, game_id)
        await call.message.edit_text(text=text, reply_markup=markup)

@dp.message_handler(state=Code, content_types=["text"])
async def state_message_all_code(message: types.Message, state: FSMContext):
    state_tr = await state.get_state()

    logging.info(f" content = {message.content_type}, id {message.from_user.id}, state {state_tr}")
    user_id = message.from_user.id
    data = await state.get_data()
    game_id = data.get("game_id")
    mission_id = data.get("mission_id")
    code_id = data.get("code_id")

    if message.text == "отмена":
        await state.reset_state(True)
        await message.answer(text="Отменил", reply_markup=ReplyKeyboardRemove())
        answer_code = await db_code.get_code(code_id=code_id)
        markup = await code_keyboard.set_codes_keyboard(code_id=code_id)
        text = f"Настройка кода: {answer_code}"
        await message.answer(text=text, reply_markup=markup)
    else:
        if state_tr == Code.Code_.state:
            new_code = message.text
            await db_code.set_code(code_id, new_code)
            await message.answer(text="Изменил код", reply_markup=ReplyKeyboardRemove())
            await state.reset_state(True)
            answer_code = await db_code.get_code(code_id=code_id)
            markup = await code_keyboard.set_codes_keyboard(code_id=code_id)
            text = f"Настройка кода: {answer_code}"
            await message.answer(text=text, reply_markup=markup)

        elif state_tr ==Code.BonusTime.state:
            time_bonus = message.text
            if await db_code.set_bonus_time(code_id, time_bonus):
                await state.reset_state(True)
                await message.answer(text="Изменил бонусное время", reply_markup=ReplyKeyboardRemove())
                answer_code = await db_code.get_code(code_id=code_id)
                markup = await code_keyboard.set_codes_keyboard(code_id=code_id)
                text = f"Настройка кода: {answer_code}"
                await message.answer(text=text, reply_markup=markup)
            else:
                await message.answer(text=f"Ты уверен что ввел все правильно?\n"
                                          f"Напоминаю, только целые числа!"
                                          f"Попробуй еще раз")

        elif state_tr == Code.Comment.state:
            comment = message.text
            await db_code.set_comment(code_id, comment)
            await state.reset_state(True)
            await message.answer(text="Добавил комментарий", reply_markup=ReplyKeyboardRemove())
            answer_code = await db_code.get_code(code_id=code_id)
            markup = await code_keyboard.set_codes_keyboard(code_id=code_id)
            text = f"Настройка кода: {answer_code}"
            await message.answer(text=text, reply_markup=markup)
