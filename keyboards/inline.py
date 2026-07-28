from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_channel_verify_keyboard(url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📢 Join Official Channel", url=url)],
            [InlineKeyboardButton(text="✅ Verify Membership", callback_data="verify_subscription")]
        ]
    )

def get_quick_crypto_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="BTC ₿", callback_data="price_bitcoin"),
                InlineKeyboardButton(text="ETH Ξ", callback_data="price_ethereum"),
                InlineKeyboardButton(text="SOL ☀️", callback_data="price_solana")
            ],
            [
                InlineKeyboardButton(text="XRP 💸", callback_data="price_ripple"),
                InlineKeyboardButton(text="BNB 🟡", callback_data="price_binancecoin"),
                InlineKeyboardButton(text="DOGE 🐶", callback_data="price_dogecoin")
            ]
        ]
    )
