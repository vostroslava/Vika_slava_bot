from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from resources.questions import GAME_QUESTIONS

router = Router()

class GameStates(StatesGroup):
    playing = State()

@router.message(F.text == "🔮 Начать игру 'Угадай Славу'")
async def start_game(message: types.Message, state: FSMContext):
    # Сбрасываем состояние и начинаем с первого вопроса (индекс 0)
    await state.set_state(GameStates.playing)
    await state.update_data(current_question=0, score=0)
    
    await ask_question(message, 0)

async def ask_question(message: types.Message, question_index: int):
    question_data = GAME_QUESTIONS[question_index]
    
    # Формируем варианты ответов
    buttons = [[KeyboardButton(text=opt)] for opt in question_data["options"]]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    
    await message.answer(
        f"❓ **Вопрос {question_index + 1}/{len(GAME_QUESTIONS)}**\n\n"
        f"{question_data['question']}",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@router.message(GameStates.playing)
async def process_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()
    current_q_index = data.get("current_question", 0)
    score = data.get("score", 0)
    
    question_data = GAME_QUESTIONS[current_q_index]
    user_answer = message.text
    
    # Проверяем ответ
    correct_option = question_data["options"][question_data["correct_option_id"]]
    
    if user_answer == correct_option:
        reaction = question_data["reaction_correct"]
        score += 1
    elif user_answer in question_data["options"]:
        reaction = question_data["reaction_wrong"]
    else:
        # Если прислали что-то левое (не из кнопок)
        await message.answer("Выбери вариант из меню! 👇")
        return

    await message.answer(reaction)
    
    # Переходим к следующему вопросу
    next_q_index = current_q_index + 1
    
    if next_q_index < len(GAME_QUESTIONS):
        await state.update_data(current_question=next_q_index, score=score)
        await ask_question(message, next_q_index)
    else:
        # Конец игры
        await state.clear()
        
        # Возвращаем главное меню
        kb = [
            [KeyboardButton(text="🔮 Сыграть еще раз")],
            [KeyboardButton(text="📊 Анализ совместимости (AI)")]
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        
        result_text = f"🎉 **Игра окончена!**\nТвой счет: {score} из {len(GAME_QUESTIONS)}.\n\n"
        if score == len(GAME_QUESTIONS):
            result_text += "Ты знаешь меня идеально! Это пугает... и восхищает. ❤️"
        elif score >= len(GAME_QUESTIONS) / 2:
            result_text += "Неплохо! Но нам есть что обсудить за кофе. 😉"
        else:
            result_text += "Кажется, нам нужно срочно встретиться и узнать друг друга получше!"
            
        await message.answer(result_text, reply_markup=keyboard, parse_mode="Markdown")
