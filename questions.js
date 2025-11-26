const TEST_DATA = {
    scales: {
        openness: {
            id: 1,
            name: "Сексуальная открытость",
            description: "Интерес к экспериментам и новизне"
        },
        connection: {
            id: 2,
            name: "Эмоциональная близость",
            description: "Важность чувств для секса"
        },
        communication: {
            id: 3,
            name: "Коммуникация",
            description: "Комфорт в обсуждении желаний"
        },
        boundaries: {
            id: 4,
            name: "Границы",
            description: "Умение говорить «нет»"
        },
        body_image: {
            id: 5,
            name: "Самопринятие",
            description: "Отношение к своему телу"
        },
        playfulness: {
            id: 6,
            name: "Игривость",
            description: "Лёгкость и юмор в сексе"
        }
    },
    questions: [
        // ШКАЛА 1: Открытость
        { id: 1, scale: "openness", reverse: false, text: "Мне интересно пробовать в сексе что-то новое, если я доверяю партнёру." },
        { id: 2, scale: "openness", reverse: false, text: "Если интимные отношения долго остаются одинаковыми, мне становится скучно." },
        { id: 3, scale: "openness", reverse: false, text: "Сексуальные фантазии и обсуждение новых идей меня возбуждают." },
        { id: 4, scale: "openness", reverse: true, text: "Мне важнее стабильность и предсказуемость в сексе, чем эксперименты." },

        // ШКАЛА 2: Близость
        { id: 5, scale: "connection", reverse: false, text: "Мне трудно заниматься сексом с человеком, к которому я ничего не чувствую." },
        { id: 6, scale: "connection", reverse: false, text: "Лучший секс для меня — когда есть глубокая эмоциональная близость." },
        { id: 7, scale: "connection", reverse: false, text: "Я могу получать удовольствие от секса без сильной любви, если есть уважение." },
        { id: 8, scale: "connection", reverse: true, text: "Эмоции для меня почти не важны, главное — физическое удовольствие." },

        // ШКАЛА 3: Коммуникация
        { id: 9, scale: "communication", reverse: false, text: "Мне легко говорить партнёру, что мне нравится в сексе." },
        { id: 10, scale: "communication", reverse: true, text: "Мне сложно прямо сказать, если в сексе мне что-то не подходит." },
        { id: 11, scale: "communication", reverse: false, text: "Я могу спокойно обсудить желание попробовать что-то новое." },
        { id: 12, scale: "communication", reverse: true, text: "Разговоры о сексе меня смущают, я предпочитаю их избегать." },

        // ШКАЛА 4: Границы
        { id: 13, scale: "boundaries", reverse: false, text: "Если мне некомфортно, я могу остановить процесс, даже если партнёру это не нравится." },
        { id: 14, scale: "boundaries", reverse: true, text: "Иногда я соглашаюсь на секс, хотя не хочу, чтобы не обидеть партнёра." },
        { id: 15, scale: "boundaries", reverse: false, text: "Для меня важно заранее обсуждать границы допустимого." },
        { id: 16, scale: "boundaries", reverse: true, text: "Мне трудно отстоять свои границы, когда партнёр настаивает." },

        // ШКАЛА 5: Самопринятие
        { id: 17, scale: "body_image", reverse: false, text: "В интимных ситуациях я чувствую себя привлекательным(ой)." },
        { id: 18, scale: "body_image", reverse: true, text: "Из-за того, как я выгляжу, мне бывает сложно расслабиться." },
        { id: 19, scale: "body_image", reverse: false, text: "Я принимаю свою сексуальность и имею право на удовольствие." },
        { id: 20, scale: "body_image", reverse: true, text: "Иногда я чувствую стыд или вину из-за своих желаний." },

        // ШКАЛА 6: Игра
        { id: 21, scale: "playfulness", reverse: false, text: "В сексе мне нравится элемент игры, шутки и лёгкий юмор." },
        { id: 22, scale: "playfulness", reverse: true, text: "Я боюсь выглядеть нелепо в сексе и стараюсь вести себя «правильно»." },
        { id: 23, scale: "playfulness", reverse: false, text: "Мне важно, чтобы близость была живой и спонтанной." },
        { id: 24, scale: "playfulness", reverse: true, text: "Я так переживаю о том, что обо мне подумают, что не могу расслабиться." }
    ]
};
