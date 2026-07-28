from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from services.market_service import MarketService
from keyboards.inline import get_quick_crypto_keyboard

router = Router()

@router.message(F.text == "🪙 Crypto Market")
@router.message(F.text == "📊 Price Check")
async def crypto_market_handler(message: Message):
    data = await MarketService.get_crypto_prices()
    if not data:
        await message.answer("⚠️ Unable to reach market data servers. Please try again.")
        return

    text = "🪙 **Live Crypto Prices**\n\n"
    for coin, info in data.items():
        price = info.get("usd", 0)
        change = info.get("usd_24h_change", 0)
        icon = "🟢" if change >= 0 else "🔴"
        text += f"• **{coin.upper()}**: `${price:,.2f}` | {icon} `{change:+.2f}%`\n"

    await message.answer(text, reply_markup=get_quick_crypto_keyboard(), parse_mode="Markdown")

@router.message(F.text == "📉 Fear & Greed")
@router.message(F.text == "📅 Economic Calendar")
async def fear_greed_handler(message: Message):
    fg = await MarketService.get_fear_and_greed()
    if fg:
        val = fg.get("value")
        classification = fg.get("value_classification")
        await message.answer(f"🧠 **Crypto Fear & Greed Index**\n\nScore: `{val}/100` ({classification})", parse_mode="Markdown")
