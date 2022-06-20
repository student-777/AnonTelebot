import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from data.config import admins
from data.content import items, get_item
from keyboards.inline.pagination import get_pages_keyboard, pagination_call, show_item
from loader import dp, db

# Клавиатура с пользователями
@dp.message_handler(Command("users"), user_id=admins)
async def show_items_handler(message: types.Message):
    users_from_db = db.select_all_users()
    for admin in admins:
        if admin == message.from_user.id:
            await message.answer(
                "Вот наши пользователи:",
                reply_markup=get_pages_keyboard(users_from_db)
            )


# Перемещение по страницам клавиатуры
@dp.callback_query_handler(pagination_call.filter(key="items"))
async def show_chosen_page(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data dict {callback_data}')
    current_page = int(callback_data.get("page"))
    markup = get_pages_keyboard(items, page=current_page)
    await call.message.edit_reply_markup(
        markup
    )


# Обработка нажатия клавиши - выбор пользователя
@dp.callback_query_handler(show_item.filter())
async def show_user(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data dict {callback_data}')
    item_id = callback_data.get("item_id")
    item = get_item(item_id)
    db.delete_current_user()
    db.add_current_user(item[0])
    # column_info = db.select_user(id=item_id, name=item[1])
    # logging.info(f"Column: tuple --> {column_info}")
    await call.message.answer(
        f"Выбран пользователь {item[1]} - {item[0]}")

    # await call.message.answer(
    #     f"Выбран пользователь {column_info[1]} - {column_info[0]}")









