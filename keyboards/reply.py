from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="📊 Price Check"), KeyboardButton(text="📰 Market News")],
        [KeyboardButton(text="📈 Technical Analysis"), KeyboardButton(text="🤖 AI Assistant")],
        [KeyboardButton(text="💹 Forex Market"), KeyboardButton(text="🪙 Crypto Market")],
        [KeyboardButton(text="🔔 Price Alerts"), KeyboardButton(text="⭐ Watchlist")],
        [KeyboardButton(text="📚 Education"), KeyboardButton(text="📅 Economic Calendar")],
        [KeyboardButton(text="👤 Profile"), KeyboardButton(text="⚙️ Settings")],
        [KeyboardButton(text="📢 Join Channel"), KeyboardButton(text="ℹ️ About")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
