import json
import telebot
from telebot import types
from config import BOT_TOKEN

# Инициализация
bot = telebot.TeleBot(BOT_TOKEN)
WEBAPP_URL = "https://vostroslava.github.io/Vika_slava_bot/"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("❤️‍🔥 Пройти тест на сексуальность", web_app=types.WebAppInfo(url=WEBAPP_URL))
    markup.add(btn)
    
    bot.send_message(
        message.chat.id,
        "Привет! 👋\n\n"
        "Это бот для глубокого анализа сексуального профиля на основе модели **Big Five**.\n\n"
        "Тест поможет понять:\n"
        "🔹 Твои истинные предпочтения\n"
        "🔹 Важность эмоций и границ\n"
        "🔹 Уровень открытости новому\n\n"
        "Нажми кнопку ниже, чтобы начать 👇",
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    try:
        data = json.loads(message.web_app_data.data)
        
        # Формируем отчет
        report = "📊 **Твой Сексуальный Профиль**\n\n"
        
        for key, value in data.items():
            score = float(value['score'])
            level_icon = "🟢" if value['level'] == 'high' else ("🟡" if value['level'] == 'mid' else "⚪️")
            
            report += f"{level_icon} **{value['name']}**: {score}/5\n"
            report += f"_{value['description']}_\n\n"
            
        report += "💡 *Совет:* Обсуди эти результаты с партнером, чтобы лучше понимать друг друга."
        
        bot.send_message(message.chat.id, report, parse_mode="Markdown")
        
    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка при обработке данных. Попробуй еще раз.")
        print(f"Error: {e}")

if __name__ == "__main__":
    print("🤖 Бот запущен!")
    bot.infinity_polling()
