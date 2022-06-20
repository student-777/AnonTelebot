import sqlite3
from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hcode
from data.config import admins
from data.content import greatings, capture_greatings
from loader import dp, db
from states import LockState
from utils.misc import rate_limit
from utils.capture import gen_capture



@rate_limit(3, 'start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_name = message.from_user.full_name
    for admin in admins:
        if admin == message.from_user.id:
            await message.answer('Bot started!')
        else:
            if message.from_user.id in db.select_users_id():
                await message.answer(f'{user_name}, ты уже в БД. Можешь теперь просто отправлять сообщения '
                                     f'не запуская бота.')
            else:
                capture_text, adding_text, result_text = gen_capture()
                text = capture_greatings.format(user_name=user_name)
                with open ('documents/capture_out.jpg', 'rb') as photo:
                    await message.reply_photo(photo, caption=text)
                db.delete_capture()
                try:
                    db.add_capture(result_text)
                except sqlite3.IntegrityError as err:
                    print(err)
                await message.answer(adding_text)
                await LockState.CapTure.set()



@dp.message_handler(state=LockState.CapTure)
async def get_capture(message: types.Message, state: FSMContext):
    user_name = message.from_user.full_name
    current_date_time = datetime.now()
    date_time = current_date_time.strftime("%d-%m-%Y %H:%M")
    insert_text = message.text.strip()
    cap_text = db.select_all_capture()

    if cap_text == insert_text:
        try:
            db.add_user(id=message.from_user.id, name=user_name, date_time=date_time)
        except sqlite3.IntegrityError as err:
            print(err)
        count = db.count_users()
        await message.answer(
            "\n".join(
                [
                    hcode(f'Привет, {user_name} и добро пожаловать!'),
                    hcode(f'Ты был занесен в базу данных.'),
                    f'Колличество абонентов в базе данных: <b>{count}</b>',
                    greatings
                ]))
    else:
        await message.answer(f'Ты ввел {insert_text}, это неверный ответ. Попробуй еще раз '
                             f'используя команду /start')
    await state.reset_state()



