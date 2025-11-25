import time
import telebot
from telebot import types
from config import BOT_TOKEN
from resources.compatibility_text import COMPATIBILITY_RESULT

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)

# URL WebApp игры
CASINO_URL = "https://vostroslava.github.io/Vika_slava_bot/"

# --- Клавиатуры ---
def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎰 Казино \"Рандеву\"", web_app=types.WebAppInfo(url=CASINO_URL))
    btn2 = types.KeyboardButton("📊 Анализ совместимости")
    markup.add(btn1)
    markup.add(btn2)
    return markup

# --- Хендлеры ---

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет, Вика! 👋\n\n"
        "Я — персональный бот-ассистент, созданный специально для тебя.\n"
        "У меня есть для тебя кое-что интересное...\n\n"
        "🎰 **Казино \"Рандеву\"** — покрути колесо и выиграй незабываемое свидание!\n"
        "📊 **Анализ совместимости** — узнай, насколько вы с ним подходите друг другу.\n\n"
        "Что выберешь?",
        reply_markup=get_main_menu(),
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['vip'])
def send_vip(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("💎 VIP Казино", web_app=types.WebAppInfo(url="https://vostroslava.github.io/Vika_slava_bot/vip.html"))
    markup.add(btn)
    
    bot.send_message(
        message.chat.id,
        "🔐 **Секретный режим активирован**\n\n"
        "Добро пожаловать в VIP-версию казино.\n"
        "Призы только для своих. 😏\n\n"
        "Готова?",
        reply_markup=markup,
        parse_mode="Markdown"
    )


@bot.message_handler(func=lambda message: message.text == "📊 Анализ совместимости")
def analysis_handler(message):
    msg = bot.send_message(message.chat.id, "🔄 Подключаюсь к нейросети...")
    time.sleep(1)
    
    bot.edit_message_text("📂 Загружаю профиль: Вика (19)...", chat_id=message.chat.id, message_id=msg.message_id)
    time.sleep(1)
    
    bot.edit_message_text("📂 Загружаю профиль: Слава (26)...", chat_id=message.chat.id, message_id=msg.message_id)
    time.sleep(1)
    
    bot.edit_message_text("🧠 Сравниваю психотипы (Big Five Model)...", chat_id=message.chat.id, message_id=msg.message_id)
    time.sleep(1.5)
    
    bot.edit_message_text("✅ Анализ завершен!", chat_id=message.chat.id, message_id=msg.message_id)
    time.sleep(0.5)
    
    bot.send_message(message.chat.id, COMPATIBILITY_RESULT, parse_mode="Markdown")

# Обработка данных из WebApp
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    # Когда Вика заберет приз в казино, бот получит уведомление
    bot.send_message(
        message.chat.id,
        "🎉 Поздравляю с выигрышем!\n\n"
        "Напиши мне, когда будешь готова забрать свой приз! 😊",
        reply_markup=get_main_menu()
    )

if __name__ == "__main__":
    print("🤖 Бот запущен (Telebot)!")
    bot.infinity_polling()
