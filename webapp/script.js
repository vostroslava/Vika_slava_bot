// Призы для колеса
const prizes = [
    { text: "🎬 Кино/мультики", emoji: "🎬", category: "Развлечения" },
    { text: "⛸️ Поход на каток", emoji: "⛸️", category: "Развлечения" },
    { text: "🎲 Настольные игры", emoji: "🎲", category: "Развлечения" },
    { text: "🌃 Вечерняя прогулка", emoji: "🌃", category: "Развлечения" },
    { text: "☕ Кофе + десерт", emoji: "☕", category: "Гастрономия" },
    { text: "🍳 Слава готовит ужин", emoji: "🍳", category: "Гастрономия" },
    { text: "🎁 Сюрприз от Славы", emoji: "🎁", category: "Сюрприз" },
    { text: "💝 Подарок-мелочь", emoji: "💝", category: "Сюрприз" },
    { text: "💆 Массаж спины 15 мин", emoji: "💆", category: "Милота" },
    { text: "👜 Слава носит сумку", emoji: "👜", category: "Милота" },
    { text: "🎥 Выбор фильма", emoji: "🎥", category: "Милота" },
    { text: "🤗 Обнимашки 24/7", emoji: "🤗", category: "Милота" }
];

// Цвета для секторов (чередование)
const colors = ['#DC143C', '#8B0000', '#B22222', '#A52A2A'];

// Элементы
const canvas = document.getElementById('wheelCanvas');
const ctx = canvas.getContext('2d');
const spinBtn = document.getElementById('spinBtn');
const resultContainer = document.getElementById('resultContainer');
const prizeText = document.getElementById('prizeText');
const claimBtn = document.getElementById('claimBtn');
const finalMessage = document.getElementById('finalMessage');
const closeBtn = document.getElementById('closeBtn');

// Параметры колеса
const centerX = canvas.width / 2;
const centerY = canvas.height / 2;
const radius = 160;
let currentRotation = 0;
let isSpinning = false;

// Рисуем колесо
function drawWheel() {
    const numPrizes = prizes.length;
    const anglePerSlice = (2 * Math.PI) / numPrizes;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < numPrizes; i++) {
        const startAngle = currentRotation + i * anglePerSlice;
        const endAngle = startAngle + anglePerSlice;

        // Рисуем сектор
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.arc(centerX, centerY, radius, startAngle, endAngle);
        ctx.closePath();
        ctx.fillStyle = colors[i % colors.length];
        ctx.fill();

        // Граница сектора (золотая)
        ctx.strokeStyle = '#FFD700';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Текст (emoji)
        ctx.save();
        ctx.translate(centerX, centerY);
        ctx.rotate(startAngle + anglePerSlice / 2);
        ctx.textAlign = 'center';
        ctx.font = '28px Arial';
        ctx.fillText(prizes[i].emoji, radius * 0.7, 10);
        ctx.restore();
    }

    // Центральный круг (декоративный)
    ctx.beginPath();
    ctx.arc(centerX, centerY, 45, 0, 2 * Math.PI);
    ctx.fillStyle = '#1a1a1a';
    ctx.fill();
    ctx.strokeStyle = '#FFD700';
    ctx.lineWidth = 4;
    ctx.stroke();
}

// Крутим колесо
function spinWheel() {
    if (isSpinning) return;

    isSpinning = true;
    spinBtn.classList.add('spinning');

    // Случайный приз
    const randomPrizeIndex = Math.floor(Math.random() * prizes.length);
    const anglePerSlice = (2 * Math.PI) / prizes.length;

    // Целевой угол (останавливается на призе)
    const targetAngle = randomPrizeIndex * anglePerSlice + anglePerSlice / 2;

    // Количество оборотов + целевой угол
    const spins = 5 + Math.random() * 3; // 5-8 оборотов
    const totalRotation = spins * 2 * Math.PI + (2 * Math.PI - targetAngle);

    let startTime = null;
    const duration = 4000; // 4 секунды

    function animate(currentTime) {
        if (!startTime) startTime = currentTime;
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);

        // Easing (замедление к концу)
        const easeOut = 1 - Math.pow(1 - progress, 3);

        currentRotation = easeOut * totalRotation;
        drawWheel();

        if (progress < 1) {
            requestAnimationFrame(animate);
        } else {
            // Остановка
            isSpinning = false;
            spinBtn.classList.remove('spinning');
            showPrize(randomPrizeIndex);
        }
    }

    requestAnimationFrame(animate);
}

// Показать приз
function showPrize(index) {
    const prize = prizes[index];
    prizeText.innerHTML = `<strong>${prize.text}</strong><br><small>(${prize.category})</small>`;

    setTimeout(() => {
        resultContainer.classList.add('show');
    }, 500);
}

// Забрать приз
claimBtn.addEventListener('click', () => {
    resultContainer.classList.remove('show');
    setTimeout(() => {
        finalMessage.classList.add('show');
    }, 300);
});

// Закрыть финальное сообщение
closeBtn.addEventListener('click', () => {
    finalMessage.classList.remove('show');

    // Отправка в Telegram (если запущено в WebApp)
    if (window.Telegram && window.Telegram.WebApp) {
        window.Telegram.WebApp.sendData(JSON.stringify({
            action: 'prize_claimed',
            prize: prizeText.textContent
        }));
    }
});

// Обработчик кнопки
spinBtn.addEventListener('click', spinWheel);

// Инициализация
drawWheel();

// Telegram WebApp integration
if (window.Telegram && window.Telegram.WebApp) {
    window.Telegram.WebApp.ready();
    window.Telegram.WebApp.expand();
}
