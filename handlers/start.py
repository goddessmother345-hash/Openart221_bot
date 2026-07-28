from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards.reply import get_main_menu_keyboard
from keyboards.inline import get_channel_verify_keyboard
from config.settings import settings

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    welcome_msg = (
        f"🚀 **Welcome to NexapTrade Bot**, {message.from_user.first_name}!\n\n"
        f"Your all-in-one AI-driven trading terminal for **Crypto & Forex** insights, real-time alerts, "
        f"and automated technical indicators.\n\n"
        f"💡 Select an option from the menu below or type `/help` to see available commands."
    )
    if settings.REQUIRED_CHANNEL_ID:
        await message.answer(
            "📢 **Channel Verification Required**\n\nPlease join our official channel to unlock full functionality.",
            reply_markup=get_channel_verify_keyboard(settings.REQUIRED_CHANNEL_URL)
        )
    else:
        await message.answer(welcome_msg, reply_markup=get_main_menu_keyboard(), parse_mode="Markdown")

@router.callback_query(F.data == "verify_subscription")
async def verify_sub(callback: CallbackQuery):
    await callback.answer("✅ Channel membership verified!", show_alert=True)
    await callback.message.answer("🎉 Access unlocked!", reply_markup=get_main_menu_keyboard())
