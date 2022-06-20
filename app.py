from loader import db
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    # import filters
    import middlewares
    import filters

    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify

    try:
        db.create_table_users()
    except Exception as err:
        print(err)

    try:
        db.create_table_current_user()
    except Exception as err:
        print(err)

    try:
        db.create_table_capture()
    except Exception as err:
        print(err)



    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
