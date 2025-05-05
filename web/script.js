let quizData = [];
let currentIndex = 0;
let bookmarks = new Set();
let answered = false;
let score = 0;
let attempted = 0;

// Get manualCode from URL
const urlParams = new URLSearchParams(window.location.search);
const manualCode = urlParams.get("manualCode");

// Load bookmarks
const stored = localStorage.getItem("bookmarks");
if (stored) bookmarks = new Set(JSON.parse(stored));

// DOM elements
const questionEl = document.getElementById("question-text");
const optionsEl = document.getElementById("option-list");
const bookmarkBtn = document.getElementById("bookmark-btn");
const nextBtn = document.getElementById("next-btn");
const scoreEl = document.getElementById("score");
const explanationBox = document.createElement("p");
explanationBox.id = "explanation";
document.getElementById("quiz-section").appendChild(explanationBox);

// Load and filter quiz data
fetch("data/quiz_data.json")
  .then((res) => res.json())
  .then((data) => {
    if (manualCode) {
      quizData = data.filter(q => q.manualCode === manualCode);
    } else {
      quizData = data;
    }

    if (quizData.length === 0) {
      questionEl.textContent = "❌ No questions found for selected manual.";
      nextBtn.style.display = "none";
    } else {
      displayQuestion();
      updateScore();
    }
  });

  // Step 1: Load manuals.json to display title
  fetch("data/manuals.json")
  .then(res => res.json())
  .then(manuals => {
    const match = manuals.find(m => m.code === manualCode);
    const heading = document.getElementById("quiz-heading");
    const subtitle = document.getElementById("manual-title");

    if (match) {
      heading.textContent = `Quiz on ${match.title}`;
      subtitle.textContent = `📘 ${match.org} (${match.year})`;
    } else {
      heading.textContent = "Full Quiz";
      subtitle.textContent = "📘 All Manuals";
    }
  });



function displayQuestion() {
  const q = quizData[currentIndex];
  answered = false;

  questionEl.textContent = q.question;
  explanationBox.textContent = "";
  explanationBox.classList.remove("show");

  bookmarkBtn.textContent = bookmarks.has(q.id) ? "★" : "☆";
  bookmarkBtn.onclick = () => {
    toggleBookmark(q.id);
    updateBookmarkIcon();
  };

  renderOptions();
}

function renderOptions() {
  const q = quizData[currentIndex];
  optionsEl.innerHTML = "";

  q.options.forEach((opt, i) => {
    const li = document.createElement("li");
    li.textContent = opt;
    li.classList.add("option");

    li.onclick = () => {
      if (!answered) {
        answered = true;
        attempted++;
        const isCorrect = i === q.correctAnswerIndex;
        if (isCorrect) score++;
        showResult(isCorrect, i, q.correctAnswerIndex, q.explanation);
        updateScore();
      }
    };

    optionsEl.appendChild(li);
  });
}

function showResult(isCorrect, selectedIndex, correctIndex, explanation) {
  const options = document.querySelectorAll(".option");
  options.forEach((opt, i) => {
    opt.classList.add("disabled");
    if (i === correctIndex) opt.classList.add("correct");
    else if (i === selectedIndex) opt.classList.add("wrong");
  });

  explanationBox.textContent = `Explanation: ${explanation}`;
  explanationBox.classList.add("show");
}

function updateScore() {
  scoreEl.textContent = `Score: ${score} / ${attempted}`;
}

function toggleBookmark(id) {
  if (bookmarks.has(id)) bookmarks.delete(id);
  else bookmarks.add(id);
  localStorage.setItem("bookmarks", JSON.stringify([...bookmarks]));
}

function updateBookmarkIcon() {
  const q = quizData[currentIndex];
  bookmarkBtn.textContent = bookmarks.has(q.id) ? "★" : "☆";
}

nextBtn.onclick = () => {
  currentIndex = (currentIndex + 1) % quizData.length;
  if (currentIndex === 0) {
    score = 0;
    attempted = 0;
  }
  displayQuestion();
};
