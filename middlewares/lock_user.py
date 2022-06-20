import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from loader import bot, db


class Blocker(BaseMiddleware):
    """
    Эта middleware блокирует юзера по id
    в pre_process_update. Вариант рабочий, декоратора не требует.
    Составленна на основе big_brother middleware
    """

    # on_pre_process_update
    async def on_pre_process_update(self, update: types.Update, data: dict):
        banned_users = db.select_block_users()

        # Проверка где находится id блокируемого юзера: сообщение или нажатие кнопки
        if update.message:
            user = update.message.from_user.id

        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return


        if user in banned_users:
            await bot.send_message(user, f'<b>Любезный {update.message.from_user.full_name}, тебя забанили\n'
                                         f'за неправильное пользование ботом!\n'
                                         f'Для решения вопроса напиши сюда: shurab@tuta.io</b>')
            raise CancelHandler()













