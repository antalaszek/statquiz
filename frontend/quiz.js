let distributions = [];
let currentQuestionIndex = 0;
let score = 0;

// DOM elements
const plotContainer = document.getElementById('plot-container');
const formulaContainer = document.getElementById('formula-container');
const answerInput = document.getElementById('answer-input');
const submitBtn = document.getElementById('submit-btn');
const nextBtn = document.getElementById('next-btn');
const feedback = document.getElementById('feedback');
const progress = document.getElementById('progress');
let studyMode = false;
const studyModeBtn = document.getElementById('study-mode-btn');
const quizModeBtn = document.getElementById('quiz-mode-btn');
const studyModeSection = document.getElementById('study-mode');
const quizContainer = document.getElementById('quiz-container');
const distributionsGrid = document.getElementById('distributions-grid');

// Load distributions data
fetch('/api/questions')
    .then(response => response.json())
    .then(data => {
        distributions = data;
        showQuestion();
      if (studyMode) renderStudyMode();
    })
    .catch(error => {
        console.error('Error loading distributions:', error);
        feedback.textContent = 'Error loading quiz data. Please try again later.';
    });
distributions = distributions.map(value => ({ value, sort: Math.random() }))
    .sort((a, b) => a.sort - b.sort)
    .map(({ value }) => value)

function showQuestion() {
    if (currentQuestionIndex >= distributions.length) {
        // Quiz completed
        plotContainer.innerHTML = `<h2>Quiz Completed!</h2><p>Your score: ${score}/${distributions.length}</p>`;
        formulaContainer.classList.add('hidden');
        answerInput.classList.add('hidden');
        submitBtn.classList.add('hidden');
        nextBtn.classList.add('hidden');
        return;
    }

    const currentDist = distributions[currentQuestionIndex];
    plotContainer.innerHTML = currentDist.svg;
    formulaContainer.classList.add('hidden');
    answerInput.value = '';
    answerInput.focus();
    feedback.textContent = '';
    updateProgress();
}

function checkAnswer() {
    const userAnswer = answerInput.value.trim().toLowerCase();
    const correctAnswer = distributions[currentQuestionIndex].name.toLowerCase();

    if (userAnswer === correctAnswer) {
        score++;
        feedback.textContent = 'Correct!';
        feedback.className = 'correct';
        showFormula();
    } else {
        feedback.textContent = `Incorrect. The correct answer is "${correctAnswer}".`;
        feedback.className = 'incorrect';
        showFormula();
    }

    submitBtn.classList.add('hidden');
    nextBtn.classList.remove('hidden');
}

function showFormula() {
    const currentDist = distributions[currentQuestionIndex];
    formulaContainer.textContent = `Density function:$$${currentDist.formula}$$`;
    formulaContainer.classList.remove('hidden');
  if (window.MathJax){
    MathJax.typesetPromise([formulaContainer]).catch(err => console.error('MathJax typesetting error:', err));
  }
  
}

function nextQuestion() {
    currentQuestionIndex++;
    submitBtn.classList.remove('hidden');
    nextBtn.classList.add('hidden');
    showQuestion();
}

function updateProgress() {
    progress.textContent = `Question ${currentQuestionIndex + 1} of ${distributions.length}`;
}

function renderStudyMode() {
    distributionsGrid.innerHTML = '';
    console.log("entering study mode")
    
    distributions.forEach(dist => {
      console.log(dist)
        const card = document.createElement('div');
        card.className = 'distribution-card';
        

  
        card.innerHTML = `
            <h3>${dist.name.charAt(0).toUpperCase() + dist.name.slice(1)} Distribution</h3>
            <div class="distribution-plot">${dist.svg}</div>
            <div class="distribution-formula">$$${dist.formula}$$</div>
            <div class="distribution-params">Parameters: ${JSON.stringify(dist.parameters)}</div>
        `;
        
      if (window.MathJax){
        MathJax.typesetPromise([card]).catch(err => console.error('MathJax typesetting error:', err));
      }
        distributionsGrid.appendChild(card);
    });
}

// Event listeners
submitBtn.addEventListener('click', checkAnswer);
nextBtn.addEventListener('click', nextQuestion);

// Allow pressing Enter to submit
answerInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        if (nextBtn.classList.contains('hidden')) {
            checkAnswer();
        } else {
            nextQuestion();
        }
    }
});

studyModeBtn.addEventListener('click', () => {
    studyMode = true;
    studyModeSection.classList.remove('hidden');
    quizContainer.classList.add('hidden');
    studyModeBtn.classList.add('hidden');
    quizModeBtn.classList.remove('hidden');
    renderStudyMode();
});

quizModeBtn.addEventListener('click', () => {
    studyMode = false;
    studyModeSection.classList.add('hidden');
    quizContainer.classList.remove('hidden');
    quizModeBtn.classList.add('hidden');
    studyModeBtn.classList.remove('hidden');
});
