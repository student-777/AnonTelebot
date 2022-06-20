import sqlite3
from datetime import datetime
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hcode
from data.config import admins
from data.content import greatings
from loader import dp, db
from utils.misc import rate_limit


@rate_limit(4, 'start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    current_date_time = datetime.now()
    date_time = current_date_time.strftime("%d-%m-%Y %H:%M")
    for admin in admins:
        if admin == message.from_user.id:
            await message.answer('Bot started')
        else:
            try:
                db.add_user(id=message.from_user.id,
                            name=name, date_time=date_time)
            except sqlite3.IntegrityError as err:
                print(err)

            count = db.count_users()
            await message.answer(
                "\n".join(
                    [
                        hcode(f'Привет, {message.from_user.full_name} и добро пожаловать!'),
                        hcode(f'Ты был занесен в базу данных.'),
                        f'Колличество абонентов в базе данных: <b>{count}</b>',
                        greatings
                    ]))

