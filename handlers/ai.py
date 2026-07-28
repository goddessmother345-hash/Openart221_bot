from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.bot_states import AIQueryState
from services.ai_service import ai_service

router = Router()

@router.message(F.text == "🤖 AI Assistant")
async def prompt_ai(message: Message, state: FSMContext):
    await state.set_state(AIQueryState.waiting_for_question)
    await message.answer("🤖 **NexapTrade AI Assistant**\n\nAsk me anything about market analysis, trading strategies, technical indicators, or candlestick patterns:")

@router.message(AIQueryState.waiting_for_question)
async def process_ai_question(message: Message, state: FSMContext):
    loading = await message.answer("🧠 *Analyzing market queries...*")
    response = await ai_service.ask_assistant(message.text)
    await loading.delete()
    await message.answer(response, parse_mode="Markdown")
    await state.clear()
