import asyncio
from aiogram import Router, types, F
from resources.compatibility_text import COMPATIBILITY_RESULT

router = Router()

@router.message(F.text == "📊 Анализ совместимости (AI)")
async def show_analysis(message: types.Message):
    # Имитация бурной деятельности ИИ
    msg = await message.answer("🔄 Подключаюсь к нейросети...")
    await asyncio.sleep(1)
    
    await msg.edit_text("📂 Загружаю профиль: Вика (19)...")
    await asyncio.sleep(1)
    
    await msg.edit_text("📂 Загружаю профиль: Слава (26)...")
    await asyncio.sleep(1)
    
    await msg.edit_text("🧠 Сравниваю психотипы (Big Five Model)...")
    await asyncio.sleep(1.5)
    
    await msg.edit_text("✅ Анализ завершен!")
    await asyncio.sleep(0.5)
    
    # Выводим результат
    await message.answer(COMPATIBILITY_RESULT, parse_mode="Markdown")
