// State
let currentQuestionIndex = 0;
let answers = {}; // {questionId: score}
const totalQuestions = TEST_DATA.questions.length;

// Telegram WebApp
const tg = window.Telegram.WebApp;
tg.expand();

// Elements
const welcomeScreen = document.getElementById('welcomeScreen');
const quizScreen = document.getElementById('quizScreen');
const resultScreen = document.getElementById('resultScreen');

const progressBar = document.getElementById('progressBar');
const currentQuestionNum = document.getElementById('currentQuestionNum');
const totalQuestionsEl = document.getElementById('totalQuestions');
const questionText = document.getElementById('questionText');
const resultsList = document.getElementById('resultsList');

// Initialize
totalQuestionsEl.textContent = totalQuestions;

function startTest() {
    welcomeScreen.classList.remove('active');
    quizScreen.classList.add('active');
    renderQuestion();
}

function renderQuestion() {
    const question = TEST_DATA.questions[currentQuestionIndex];

    // Update UI
    currentQuestionNum.textContent = currentQuestionIndex + 1;
    questionText.textContent = question.text;

    // Progress bar
    const progress = ((currentQuestionIndex) / totalQuestions) * 100;
    progressBar.style.width = `${progress}%`;
}

function selectOption(value) {
    const question = TEST_DATA.questions[currentQuestionIndex];
    answers[question.id] = value;

    // Next question or finish
    if (currentQuestionIndex < totalQuestions - 1) {
        currentQuestionIndex++;

        // Small animation for transition
        questionText.style.opacity = 0;
        setTimeout(() => {
            renderQuestion();
            questionText.style.opacity = 1;
        }, 200);
    } else {
        finishTest();
    }
}

function finishTest() {
    quizScreen.classList.remove('active');
    resultScreen.classList.add('active');

    const results = calculateResults();
    renderResults(results);

    // Send data to Telegram
    if (tg) {
        tg.sendData(JSON.stringify(results));
    }
}

function calculateResults() {
    const scaleScores = {};
    const scaleCounts = {};

    // Initialize
    for (const key in TEST_DATA.scales) {
        scaleScores[key] = 0;
        scaleCounts[key] = 0;
    }

    // Calculate
    TEST_DATA.questions.forEach(q => {
        const rawScore = answers[q.id];
        let finalScore = rawScore;

        if (q.reverse) {
            finalScore = 6 - rawScore;
        }

        scaleScores[q.scale] += finalScore;
        scaleCounts[q.scale]++;
    });

    // Average
    const finalResults = {};
    for (const key in TEST_DATA.scales) {
        const avg = scaleScores[key] / scaleCounts[key];
        let level = 'mid';
        if (avg <= 2.4) level = 'low';
        else if (avg >= 3.5) level = 'high';

        finalResults[key] = {
            name: TEST_DATA.scales[key].name,
            score: avg.toFixed(1),
            level: level,
            description: TEST_DATA.scales[key].description
        };
    }

    return finalResults;
}

function renderResults(results) {
    resultsList.innerHTML = '';

    for (const key in results) {
        const res = results[key];
        const percent = (res.score / 5) * 100;

        let levelText = '';
        if (res.level === 'low') levelText = 'Низкий';
        if (res.level === 'mid') levelText = 'Средний';
        if (res.level === 'high') levelText = 'Высокий';

        const html = `
            <div class="result-item">
                <div class="res-top">
                    <span class="res-name">${res.name}</span>
                    <span class="res-score">${res.score} / 5</span>
                </div>
                <div class="res-bar-bg">
                    <div class="res-bar-fill" style="width: ${percent}%"></div>
                </div>
                <div class="res-desc">
                    Уровень: <strong>${levelText}</strong><br>
                    ${res.description}
                </div>
            </div>
        `;

        resultsList.innerHTML += html;
    }
}

function closeApp() {
    if (tg) {
        tg.close();
    }
}
