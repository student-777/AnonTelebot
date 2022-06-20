from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode

from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from data.content import often_text
from data.config import admins
from loader import dp, db
from states import LockState


# Передача общего сообщения всем пользователям в БД
@dp.message_handler(Command("broadcast"), user_id=admins)
async def get_one_user(message: types.Message):
    await message.answer(hcode("Введи текст сообщения которое хочешь передать всем:"))
    await LockState.BroadCast.set()


@dp.message_handler(state=LockState.BroadCast)
async def broadcast_message(message: types.Message, state=FSMContext):
    broadcast_text = message.text
    users_from_db = db.select_all_users()
    for user in users_from_db:
        (usr_id, usr_name, usr_data, usr_state) = user
        await bot.send_message(usr_id, f"Дорогой пользователь бота <b>{usr_name}!</b> {broadcast_text}")
        await message.answer(hcode("Сообщение отправленно!"))
    await state.finish()
