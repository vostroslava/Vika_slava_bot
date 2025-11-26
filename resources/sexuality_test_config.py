# -*- coding: utf-8 -*-

"""
Модуль конфигурации теста на сексуальность (Sexuality Module based on Big Five).
Содержит структуру вопросов, шкал и логику подсчета баллов.
"""

SEXUALITY_TEST_STRUCTURE = {
    "meta": {
        "name": "Sexuality & Big Five Integration Module",
        "version": "1.0",
        "description": "Опросник из 24 утверждений для оценки сексуального профиля по 6 шкалам."
    },
    "scales": {
        "openness": {
            "id": 1,
            "code": "openness",
            "name": "Сексуальная открытость и новизна",
            "description": "Интерес к экспериментам, разнообразию и новым сценариям."
        },
        "connection": {
            "id": 2,
            "code": "connection",
            "name": "Эмоциональная близость",
            "description": "Важность чувств и глубокой связи для сексуального удовлетворения."
        },
        "communication": {
            "id": 3,
            "code": "communication",
            "name": "Комфорт разговоров о сексе",
            "description": "Умение обсуждать желания, фантазии и неудобные моменты."
        },
        "boundaries": {
            "id": 4,
            "code": "boundaries",
            "name": "Границы и безопасность",
            "description": "Умение говорить «нет» и защищать свой комфорт."
        },
        "body_image": {
            "id": 5,
            "code": "body_image",
            "name": "Самопринятие тела и сексуальности",
            "description": "Отсутствие стыда, принятие своего права на удовольствие."
        },
        "playfulness": {
            "id": 6,
            "code": "playfulness",
            "name": "Игра и лёгкость",
            "description": "Наличие юмора, спонтанности и отсутствие страха выглядеть нелепо."
        }
    },
    "questions": [
        # ШКАЛА 1: Открытость
        {"id": 1, "scale_code": "openness", "reverse": False, "text": "Мне интересно пробовать в сексе что-то новое, если я доверяю партнёру и чувствую себя в безопасности."},
        {"id": 2, "scale_code": "openness", "reverse": False, "text": "Если наши интимные отношения долго остаются одинаковыми, мне со временем становится скучно."},
        {"id": 3, "scale_code": "openness", "reverse": False, "text": "Сексуальные фантазии и обсуждение новых идей скорее возбуждают меня, чем пугают или смущают."},
        {"id": 4, "scale_code": "openness", "reverse": True,  "text": "Мне гораздо важнее стабильность и предсказуемость в сексе, чем эксперименты."},
        
        # ШКАЛА 2: Близость
        {"id": 5, "scale_code": "connection", "reverse": False, "text": "Мне трудно заниматься сексом с человеком, к которому я ничего не чувствую."},
        {"id": 6, "scale_code": "connection", "reverse": False, "text": "Лучший секс для меня — когда есть эмоциональная близость и доверие."},
        {"id": 7, "scale_code": "connection", "reverse": False, "text": "Я могу получать удовольствие от секса, даже если эмоциональная связь не очень сильная, если есть взаимное согласие и уважение."},
        {"id": 8, "scale_code": "connection", "reverse": True,  "text": "Эмоции для меня почти не важны, главное — физическое удовольствие."},
        
        # ШКАЛА 3: Коммуникация
        {"id": 9, "scale_code": "communication", "reverse": False, "text": "Мне относительно легко говорить партнёру, что мне нравится в сексе."},
        {"id": 10, "scale_code": "communication", "reverse": True,  "text": "Мне сложно прямо сказать, если в сексе мне что-то не подходит."},
        {"id": 11, "scale_code": "communication", "reverse": False, "text": "Я могу спокойно обсудить с партнёром желание попробовать что-то новое в сексе."},
        {"id": 12, "scale_code": "communication", "reverse": True,  "text": "Разговоры о сексе меня скорее смущают, и я предпочитаю их избегать."},
        
        # ШКАЛА 4: Границы
        {"id": 13, "scale_code": "boundaries", "reverse": False, "text": "Если в интимной ситуации мне некомфортно, я могу остановить процесс или сказать «нет», даже если партнёру это не понравится."},
        {"id": 14, "scale_code": "boundaries", "reverse": True,  "text": "Иногда я соглашаюсь на сексуальный контакт, хотя не очень хочу, чтобы не обидеть партнёра."},
        {"id": 15, "scale_code": "boundaries", "reverse": False, "text": "Для меня важно заранее обсуждать с партнёром границы: что для меня точно недопустимо."},
        {"id": 16, "scale_code": "boundaries", "reverse": True,  "text": "Мне трудно отстоять свои границы, когда партнёр настаивает на сексе или каких-то практиках."},
        
        # ШКАЛА 5: Самопринятие
        {"id": 17, "scale_code": "body_image", "reverse": False, "text": "В интимных ситуациях я чаще чувствую себя привлекательным(ой), чем неуверенным(ой) в себе."},
        {"id": 18, "scale_code": "body_image", "reverse": True,  "text": "Из-за того, как я выгляжу, мне бывает сложно расслабиться в сексе."},
        {"id": 19, "scale_code": "body_image", "reverse": False, "text": "В целом я принимаю свою сексуальность и считаю, что имею право получать удовольствие."},
        {"id": 20, "scale_code": "body_image", "reverse": True,  "text": "Иногда я чувствую стыд или вину из-за своих сексуальных желаний, даже если они никому не вредят."},
        
        # ШКАЛА 6: Игра
        {"id": 21, "scale_code": "playfulness", "reverse": False, "text": "В сексе мне нравится элемент игры: шутки, дурачество, лёгкий юмор."},
        {"id": 22, "scale_code": "playfulness", "reverse": True,  "text": "Я боюсь выглядеть нелепо в сексе и стараюсь вести себя «правильно»."},
        {"id": 23, "scale_code": "playfulness", "reverse": False, "text": "Мне важно, чтобы интимная близость была не только серьёзной и страстной, но и живой, с местом для спонтанности."},
        {"id": 24, "scale_code": "playfulness", "reverse": True,  "text": "Я так переживаю, как я выгляжу и что обо мне подумают, что мне трудно расслабиться и получать удовольствие."}
    ]
}

def calculate_score(answers: dict) -> dict:
    """
    Подсчитывает результаты по шкалам.
    
    Args:
        answers (dict): Словарь {question_id: score (1-5)}
        
    Returns:
        dict: {scale_code: {"score": float, "level": str}}
    """
    results = {}
    
    # Инициализация счетчиков
    scale_totals = {code: 0 for code in SEXUALITY_TEST_STRUCTURE["scales"]}
    scale_counts = {code: 0 for code in SEXUALITY_TEST_STRUCTURE["scales"]}
    
    for q in SEXUALITY_TEST_STRUCTURE["questions"]:
        q_id = q["id"]
        if q_id not in answers:
            continue
            
        raw_score = answers[q_id]
        
        # Обратное кодирование
        if q["reverse"]:
            final_score = 6 - raw_score
        else:
            final_score = raw_score
            
        scale_code = q["scale_code"]
        scale_totals[scale_code] += final_score
        scale_counts[scale_code] += 1
        
    # Расчет средних и уровней
    for code in scale_totals:
        if scale_counts[code] == 0:
            results[code] = {"score": 0, "level": "unknown"}
            continue
            
        avg_score = scale_totals[code] / scale_counts[code]
        
        if avg_score <= 2.4:
            level = "low"
        elif avg_score <= 3.4:
            level = "mid"
        else:
            level = "high"
            
        results[code] = {
            "score": round(avg_score, 2),
            "level": level,
            "name": SEXUALITY_TEST_STRUCTURE["scales"][code]["name"]
        }
        
    return results
