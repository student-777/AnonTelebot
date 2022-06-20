

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


@dp.message_handler(Command("lock"), user_id=admins)
async def get_user(message: types.Message):
   await message.answer(hcode("Введи id пользователя, которого нужно забанить.\n"
                              "Вводятся только цифры без пробела."))
   await LockState.LockId.set()




@dp.message_handler(state=LockState.LockId)
async def lock_user(message: types.Message, state: FSMContext):
    lock_id = message.text.strip()
    try:
        lock_id = int(lock_id)
        lock_username = db.select_user(id=lock_id)[1]
        if lock_id in db.select_users_id():
            db.update_user_state(id=lock_id, state=True)
            await message.answer(hcode(f'Пользователь {lock_username} --> {lock_id} заблокирован.'))
    except:
        await message.answer(hcode(often_text))
    # await state.finish()
    await state.reset_state()


