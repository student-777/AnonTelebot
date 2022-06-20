# Добавляем пользователя зная его user id и желательно user name
# Не работает, так как бот не может писать первым! Сделал в качестве упражнения.

from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from aiogram import types
from aiogram.dispatcher.filters import Command
from data.config import admins
from loader import dp, db
from states import AddUsr
from datetime import datetime


@dp.message_handler(Command("addusr"), user_id=admins)
async def add_usr_id(message: types.Message):
   await message.answer(hcode("Введи id пользователя, которого нужно добавить.\n"
                              "Вводятся только цифры без пробела."))
   await AddUsr.addusr_id.set()



@dp.message_handler(state=AddUsr.addusr_id)
async def add_usr_name(message: types.Message, state: FSMContext):
    usr_id = message.text.strip()
    if len(usr_id) >= 8:
        try:
            usr_id_int = int(usr_id)
            await message.answer(hcode('Введи имя пользователя, которого нужно добавить.'))
            await state.update_data({"usr_id": usr_id_int})
            await AddUsr.addusr_name.set()
        except:
            await message.answer(hcode('id пользователя должен содержать только цифры! '
                                       'Попробуй еще раз через команду /addusr'))
            await state.reset_state()
    else:
        await message.answer(hcode('Длинна id пользователя должена быть не менее 8-ми цифр. '
                                   'Попробуй еще раз через команду /addusr'))
        await state.reset_state()



@dp.message_handler(state=AddUsr.addusr_name)
async def record_to_db(message: types.Message, state: FSMContext):
    usr_data = await state.get_data()
    usr_id = usr_data.get('usr_id')
    usr_name = message.text
    current_date_time = datetime.now()
    date_time = current_date_time.strftime("%d-%m-%Y %H:%M")
    try:
        db.add_user(id=usr_id, name=usr_name, date_time=date_time)
        await message.answer(hcode(f'Пользователь {usr_name} --> {usr_id} добавлен в БД.'))
        await state.reset_state()
    except:
        await message.answer(hcode(f'Пользователь {usr_name} --> {usr_id} уже находится в БД.'))
        await state.reset_state()








