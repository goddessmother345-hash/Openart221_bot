from aiogram.fsm.state import State, StatesGroup

class AIQueryState(StatesGroup):
    waiting_for_question = State()

class AlertState(StatesGroup):
    waiting_for_symbol = State()
    waiting_for_price = State()

class AdminBroadcastState(StatesGroup):
    waiting_for_message = State()
