from aiogram import types
from aiogram.utils.markdown import hcode

from loader import dp, db, bot
from data.config import admins
from data.content import permitted





# Обработка текстовых сообщений от юзера к админу и обратно
# Сюда летят все текстовые сообщения
@dp.message_handler(content_types=types.ContentTypes.TEXT, user_id=permitted())
async def user_from_admin(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    current_user_id = db.select_all_current_user()
    current_user_name = db.select_user(id=current_user_id)[1]
    user_text = message.text
    text_to_admin = hcode(f"Send from {user_name} --> {user_id}:") + '\n' + f"<i>{user_text}</i>"
    for admin in admins:
        # Отправка сообщения от пользователя админу
        if user_id != admin:
            await bot.send_message(admin, text_to_admin)
            await message.reply(hcode('Send!'))
        # Отправка сообщения от админа пользователю
        else:
            text = f"<i>{user_text}</i>"
            await bot.send_message(current_user_id, text)
            await bot.send_message(admin, hcode(f"Send to {current_user_name} --> {current_user_id}"))






