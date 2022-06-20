from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import admins
from loader import dp
from utils.misc import rate_limit


@rate_limit(3, 'help')
@dp.message_handler(CommandHelp(), user_id=admins)
async def bot_help(message: types.Message):
    text = [
        '<b>Список команд: </b>',
        '<b>/broadcast</b> - Отправка сообщения всем пользователям.',
        '<b>/countusr</b> - Колличество пользователей в БД',
        '<b>/users</b> - Список пользователей для отправки сообщений.',
        '<b>/lock</b> - Блокировать пользователя.',
        '<b>/unlock</b> - Разблокировать пользователя.',
        '<b>/addusr</b> - Добавить пользователя.',
        '<b>/usersdb</b> - Чтение БД.',
        '<b>/deluser</b> - Удаление пользователя из БД.',
        '<b>/cleardb</b> - Полная очистка БД.'
    ]
    await message.answer('\n'.join(text))
