from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    # Создаем клавиатуру
    kb = [
        [KeyboardButton(text="🔮 Начать игру 'Угадай Славу'")],
        [KeyboardButton(text="📊 Анализ совместимости (AI)")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer(
        "Привет, Вика! 👋\n\n"
        "Я — персональный бот-ассистент, созданный специально для тебя.\n"
        "У меня есть доступ к секретным данным и аналитике.\n\n"
        "С чего начнем?",
        reply_markup=keyboard
    )
