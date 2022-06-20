import logging
from aiogram import types
from aiogram.utils.markdown import hcode

from data.config import admins
from data.content import permitted
from loader import dp, bot, db



# Хендлер, куда летят документы и фото .jpg, .jpeg
@dp.message_handler(content_types=types.ContentType.DOCUMENT, user_id=permitted())
async def get_document_jpg(message: types.Message):
    """Хендлер слышит формат документов и фото .jpg, .jpeg
    причем фото передает как файлы!"""

    user_name = message.from_user.full_name
    user_id = message.from_user.id
    caption = message.caption
    current_user_id = db.select_all_current_user()
    current_user_name = db.select_user(id=current_user_id)[1]
    text_to_admin = hcode(f"Send from {user_name} --> {user_id}")

    for admin in admins:
        # Отправка сообщения от пользователя админу - мне.
        if user_id != admin:
            # await message.document.download()
            await bot.send_document(admin, message.document.file_id, caption=caption)
            await message.answer('Send!')
            await bot.send_message(admin, text_to_admin)
        # Отправка сообщения от админа пользователю
        else:
            # await message.document.download()
            await bot.send_document(current_user_id, message.document.file_id, caption=caption)
            await bot.send_message(admin, hcode(f"Send to {current_user_name} --> {current_user_id}"))




# Хендлер для фото
@dp.message_handler(content_types=types.ContentType.PHOTO, user_id=permitted())
async def get_photo_png(message: types.Message):
    """Хендлер слышит только .png"""
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    caption = message.caption
    current_user_id = db.select_all_current_user()
    current_user_name = db.select_user(id=current_user_id)[1]
    text_to_admin = hcode(f"Send from {user_name} --> {user_id}")

    for admin in admins:
        # Отправка сообщения от пользователя админу - мне
        if user_id != admin:
            # await message.photo[-1].download()
            await bot.send_photo(admin, message.photo[-1].file_id, caption=caption)
            await message.answer('Send!')
            await bot.send_message(admin, text_to_admin)
        # Отправка сообщения от админа пользователю
        else:
            # await message.photo[-1].download()
            await bot.send_photo(current_user_id, message.photo[-1].file_id, caption=caption)
            await bot.send_message(admin, hcode(f"Send to {current_user_name} --> {current_user_id}"))




# Хендлер, куда летят видео
@dp.message_handler(content_types=types.ContentType.VIDEO, user_id=permitted())
async def get_video(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    caption = message.caption
    current_user_id = db.select_all_current_user()
    current_user_name = db.select_user(id=current_user_id)[1]
    text_to_admin = hcode(f"Send from {user_name} --> {user_id}")

    for admin in admins:
        # Отправка сообщения от пользователя админу - мне
        if user_id != admin:
            await bot.send_video(admin, video=message.video.file_id, caption=caption)
            await message.answer('Send!')
            await bot.send_message(admin, text_to_admin)
        # Отправка сообщения от админа пользователю
        else:
            await bot.send_video(current_user_id, video=message.video.file_id, caption=caption)
            await bot.send_message(admin, hcode(f"Send to {current_user_name} --> {current_user_id}"))




# Хендлер, куда летит аудио
@dp.message_handler(content_types=types.ContentType.AUDIO, user_id=permitted())
async def get_audio(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    caption = message.caption
    current_user_id = db.select_all_current_user()
    current_user_name = db.select_user(id=current_user_id)[1]
    text_to_admin = hcode(f"Send from {user_name} --> {user_id}")

    for admin in admins:
        # Отправка сообщения от пользователя админу - мне
        if user_id != admin:
            # await message.audio.download()
            await bot.send_audio(admin, message.audio.file_id, caption=caption)
            await message.answer('Send!')
            await bot.send_message(admin, text_to_admin)
        # Отправка сообщения от админа пользователю
        else:
            # await message.audio.download()
            await bot.send_audio(current_user_id, message.audio.file_id, caption=caption)
            await bot.send_message(admin, hcode(f"Send to {current_user_name} --> {current_user_id}"))



# Хендлер, куда летят голосовухи
@dp.message_handler(content_types=types.ContentType.VOICE, user_id=permitted())
async def get_voice(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    duration = message.voice.duration
    current_user_id = db.select_all_current_user()
    current_user_name = db.select_user(id=current_user_id)[1]
    text_to_admin = hcode(f"Send from {user_name} --> {user_id}")

    for admin in admins:
        # Отправка сообщения от пользователя админу - мне
        if user_id != admin:
            await bot.send_voice(admin, message.voice.file_id, duration=duration)
            await message.answer('Send!')
            await bot.send_message(admin, text_to_admin)
        # Отправка сообщения от админа пользователю
        else:
            await bot.send_voice(current_user_id, message.voice.file_id, duration=duration)
            await bot.send_message(admin, hcode(f"Send to {current_user_name} --> {current_user_id}"))




# Хендлер, куда летит стикер
@dp.message_handler(content_types=types.ContentType.STICKER, user_id=permitted())
async def get_sticker(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    current_user_id = db.select_all_current_user()
    current_user_name = db.select_user(id=current_user_id)[1]
    text_to_admin = hcode(f"Send from {user_name} --> {user_id}")

    for admin in admins:
        # Отправка сообщения от пользователя админу - мне
        if user_id != admin:
            await bot.send_sticker(admin, message.sticker.file_id)
            await message.answer('Send!')
            await bot.send_message(admin, text_to_admin)
        # Отправка сообщения от админа пользователю
        else:
            await bot.send_sticker(current_user_id, message.sticker.file_id)
            await bot.send_message(admin, hcode(f"Send to {current_user_name} --> {current_user_id}"))




# Хендлер, куда летит анимация - gif
@dp.message_handler(content_types=types.ContentTypes.ANIMATION, user_id=permitted())
async def get_animation(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    current_user_id = db.select_all_current_user()
    current_user_name = db.select_user(id=current_user_id)[1]
    text_to_admin = hcode(f"Send from {user_name} --> {user_id}")

    for admin in admins:
        # Отправка сообщения от пользователя админу - мне
        if user_id != admin:
            await bot.send_animation(admin, message.animation.file_id)
            await message.answer('Send!')
            await bot.send_message(admin, text_to_admin)
        # Отправка сообщения от админа пользователю
        else:
            await bot.send_animation(current_user_id, message.animation.file_id)
            await bot.send_message(admin, hcode(f"Send to {current_user_name} --> {current_user_id}"))










