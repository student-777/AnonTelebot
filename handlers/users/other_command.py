
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


# Чтение всей БД
@dp.message_handler(Command("usersdb"), user_id=admins)
async def get_usersdb(message: types.Message):
    full_db = db.select_all_users()
    for user_column in full_db:
        res_message = f"<b>id: {user_column[0]}, name: {user_column[1]}, data: {user_column[2]}, state: {user_column[3]}</b>"
        await message.answer(res_message)



# Колличество пользователей в БД
@dp.message_handler(Command("countusr"), user_id=admins)
async def usr_quantity(message: types.Message):
    quantity = db.count_users()
    await message.answer(hcode(f"Колличество пользователей в БД: {quantity}"))



# Удаление отдельного пользователя из БД
@dp.message_handler(Command("deluser"), user_id=admins)
async def get_one_user(message: types.Message):
    await message.answer(hcode("Введи id пользователя, которого нужно удалить из БД.\n"
                               "Вводятся только цифры без пробела."))
    await LockState.DelOneUser.set()


@dp.message_handler(state=LockState.DelOneUser)
async def delete_one_user(message: types.Message, state: FSMContext):
    del_usr_id = message.text.strip()

    try:
        del_usr_id = int(del_usr_id)
        del_username = db.select_user(id=del_usr_id)[1]
        if del_usr_id in db.select_users_id():
            db.delete_one_user(id=del_usr_id)
            await message.answer(hcode(f"Пользователь {del_username} --> {del_usr_id} удален из БД."))
    except:
        await message.answer(hcode(often_text))
    await state.reset_state()




# Полная очистка таблицы Users БД
@dp.message_handler(Command("cleardb"), user_id=admins)
async def clear_db(message: types.Message):
    db.delete_users()
    await message.answer(hcode("Таблица Users полностью очищенна."))










