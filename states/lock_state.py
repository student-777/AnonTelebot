from aiogram.dispatcher.filters.state import StatesGroup, State


class LockState(StatesGroup):
    LockId = State()
    UnlockId = State()
    DelOneUser = State()
    BroadCast = State()
    CapTure = State()

class AddUsr(StatesGroup):
    addusr_id = State()
    addusr_name = State()

