
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


@dp.message_handler(Command("unlock"), user_id=admins)
async def get_user(message: types.Message):
   await message.answer(hcode("Введи id пользователя, которого нужно разабанить.\n"
                              "Вводятся только цифры без пробела."))
   await LockState.UnlockId.set()




@dp.message_handler(state=LockState.UnlockId)
async def unlock_user(message: types.Message, state: FSMContext):
    unlock_id = message.text.strip()

    try:
        unlock_id = int(unlock_id)
        unlock_username = db.select_user(id=unlock_id)[1]
        if unlock_id in db.select_users_id():
            db.update_user_state(id=unlock_id, state=False)
            await message.answer(hcode(f'Пользователь {unlock_username} --> {unlock_id} разблокирован.'))
    except:
        await message.answer(hcode(often_text))
    # await state.finish()
    await state.reset_state()


