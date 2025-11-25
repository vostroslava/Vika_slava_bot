// VIP Призы для колеса
const prizes = [
    { text: "💰 Выходной (без клиентов!)", emoji: "💰", category: "Отдых" },
    { text: "🍾 Корпоратив вдвоём", emoji: "🍾", category: "Развлечения" },
    { text: "📈 Повышение на 20%", emoji: "📈", category: "Премии" },
    { text: "🏝️ Отпуск за счёт фирмы", emoji: "🏝️", category: "Отдых" },
    { text: "💎 VIP-клиент на выбор", emoji: "💎", category: "Работа" },
    { text: "🚗 Развозка туда-обратно", emoji: "🚗", category: "VIP" },
    { text: "🎭 День без соцсетей", emoji: "🎭", category: "Отдых" },
    { text: "💅 СПА за счёт босса", emoji: "💅", category: "Премии" },
    { text: "🎁 Бонус от начальства", emoji: "🎁", category: "Премии" },
    { text: "⏰ Свободный график на неделю", emoji: "⏰", category: "VIP" },
    { text: "🌹 Романтический ужин (off duty)", emoji: "🌹", category: "Романтика" },
    { text: "💵 Премия просто так", emoji: "💵", category: "Премии" }
];

// Цвета для секторов (VIP стиль - фиолетовые и золотые тона)
const colors = ['#4B0082', '#6A0DAD', '#8B008B', '#9370DB'];

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
        ctx.font = '24px Arial';
        ctx.fillText(prizes[i].emoji, radius * 0.7, 10);
        ctx.restore();
    }

    // Центральный круг
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

    const randomPrizeIndex = Math.floor(Math.random() * prizes.length);
    const anglePerSlice = (2 * Math.PI) / prizes.length;
    const targetAngle = randomPrizeIndex * anglePerSlice + anglePerSlice / 2;
    const spins = 5 + Math.random() * 3;
    const totalRotation = spins * 2 * Math.PI + (2 * Math.PI - targetAngle);

    let startTime = null;
    const duration = 4000;

    function animate(currentTime) {
        if (!startTime) startTime = currentTime;
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easeOut = 1 - Math.pow(1 - progress, 3);

        currentRotation = easeOut * totalRotation;
        drawWheel();

        if (progress < 1) {
            requestAnimationFrame(animate);
        } else {
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

// Закрыть
closeBtn.addEventListener('click', () => {
    finalMessage.classList.remove('show');

    if (window.Telegram && window.Telegram.WebApp) {
        window.Telegram.WebApp.sendData(JSON.stringify({
            action: 'vip_prize_claimed',
            prize: prizeText.textContent
        }));
    }
});

spinBtn.addEventListener('click', spinWheel);

// Инициализация
drawWheel();

if (window.Telegram && window.Telegram.WebApp) {
    window.Telegram.WebApp.ready();
    window.Telegram.WebApp.expand();
}
