from aiogram import Dispatcher

from .lock_user import Blocker
from .throttling import ThrottlingMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(Blocker())
    dp.middleware.setup(ThrottlingMiddleware())

