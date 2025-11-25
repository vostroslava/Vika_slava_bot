import time
import telebot
from telebot import types
from config import BOT_TOKEN
from resources.questions import GAME_QUESTIONS
from resources.compatibility_text import COMPATIBILITY_RESULT

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)

# Хранилище состояний для игры: {user_id: {"question_index": 0, "score": 0}}
user_data = {}

# --- Клавиатуры ---
def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔮 Начать игру 'Угадай Славу'")
    btn2 = types.KeyboardButton("📊 Анализ совместимости (AI)")
    markup.add(btn1, btn2)
    return markup

def get_game_keyboard(options):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for opt in options:
        markup.add(types.KeyboardButton(opt))
    return markup

# --- Хендлеры ---

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет, Вика! 👋\n\n"
        "Я — персональный бот-ассистент, созданный специально для тебя.\n"
        "У меня есть доступ к секретным данным и аналитике.\n\n"
        "С чего начнем?",
        reply_markup=get_main_menu()
    )

@bot.message_handler(func=lambda message: message.text == "📊 Анализ совместимости (AI)")
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

@bot.message_handler(func=lambda message: message.text == "🔮 Начать игру 'Угадай Славу'")
def start_game(message):
    user_data[message.chat.id] = {"question_index": 0, "score": 0}
    ask_question(message.chat.id)

def ask_question(chat_id):
    data = user_data.get(chat_id)
    if not data:
        return

    q_index = data["question_index"]
    if q_index >= len(GAME_QUESTIONS):
        finish_game(chat_id)
        return

    question = GAME_QUESTIONS[q_index]
    markup = get_game_keyboard(question["options"])
    
    msg = bot.send_message(
        chat_id,
        f"❓ **Вопрос {q_index + 1}/{len(GAME_QUESTIONS)}**\n\n{question['question']}",
        reply_markup=markup,
        parse_mode="Markdown"
    )
    bot.register_next_step_handler(msg, process_answer)

def process_answer(message):
    chat_id = message.chat.id
    data = user_data.get(chat_id)
    if not data:
        return # Если состояние потеряно

    q_index = data["question_index"]
    question = GAME_QUESTIONS[q_index]
    
    user_answer = message.text
    correct_option = question["options"][question["correct_option_id"]]
    
    if user_answer == correct_option:
        reaction = question["reaction_correct"]
        data["score"] += 1
    elif user_answer in question["options"]:
        reaction = question["reaction_wrong"]
    else:
        bot.send_message(chat_id, "Выбери вариант из меню! 👇")
        # Повторяем вопрос
        ask_question(chat_id)
        return

    bot.send_message(chat_id, reaction)
    
    # Следующий вопрос
    data["question_index"] += 1
    ask_question(chat_id)

def finish_game(chat_id):
    data = user_data.get(chat_id)
    score = data["score"]
    total = len(GAME_QUESTIONS)
    
    result_text = f"🎉 **Игра окончена!**\nТвой счет: {score} из {total}.\n\n"
    if score == total:
        result_text += "Ты знаешь меня идеально! Это пугает... и восхищает. ❤️"
    elif score >= total / 2:
        result_text += "Неплохо! Но нам есть что обсудить за кофе. 😉"
    else:
        result_text += "Кажется, нам нужно срочно встретиться и узнать друг друга получше!"
    
    bot.send_message(chat_id, result_text, reply_markup=get_main_menu(), parse_mode="Markdown")
    # Очищаем данные
    if chat_id in user_data:
        del user_data[chat_id]

if __name__ == "__main__":
    print("🤖 Бот запущен (Telebot)!")
    bot.infinity_polling()
