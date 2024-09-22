const deck = document.querySelectorAll(".card");
deck.forEach((card) => card.addEventListener("click", flipCard));

shuffleDeck(); // randomizes the board before each game

const displayScore1 = document.querySelector("#score1");
const displayScore2 = document.querySelector("#score2");
let gameOverMsg = document.querySelector("#memoryID");

const player1Element = document.querySelector(".Player1");
const player2Element = document.querySelector(".Player2");

let score1 = 0;
let score2 = 0;
let isFirstCard = false;
let first, second;
let isBoardClosed = false;
let p1Turn = true;

function updatePlayerTurn() {
  if (p1Turn) {
    player1Element.classList.add("current-player");
    player2Element.classList.remove("current-player");
  } else {
    player1Element.classList.remove("current-player");
    player2Element.classList.add("current-player");
  }
}

function shuffleDeck() {
  deck.forEach((card) => {
    let randomIndex = Math.floor(Math.random() * 54);
    card.style.order = randomIndex;
  });
}

function flipCard() {
  if (isBoardClosed) return;
  if (this === first) return;

  this.classList.add("flip");

  if (!isFirstCard) {
    isFirstCard = true; //first click
    first = this; // 'this' = the element that has fired the event
    return;
  }

  isFirstCard = false; //second click
  second = this;

  // if the second card has been chosen, check if they match
  checkMatch();
}

function checkMatch() {
  if (first.dataset.id == second.dataset.id) {
    first.removeEventListener("click", flipCard);
    second.removeEventListener("click", flipCard);
    removeCards(first, second);

    resetBoard();

    if (p1Turn) {
      score1 += 2;
      displayScore1.textContent = score1.toString();
    } else {
      score2 += 2;
      displayScore2.textContent = score2.toString();
    }
    checkGameOver();
  } else {
    isBoardClosed = true;
    setTimeout(() => {
      first.classList.remove("flip");
      second.classList.remove("flip");
      isBoardClosed = false;
      resetBoard();
    }, 1000);

    p1Turn = !p1Turn;
    updatePlayerTurn();
  }
}

function removeCards(first, second) {
  setTimeout(() => {
    first.innerHTML = "";
    first.style.backgroundImage = "none";
    first.style.backgroundColor = "transparent";
    second.innerHTML = "";
    second.style.backgroundImage = "none";
    second.style.backgroundColor = "transparent";
  }, 600);
}

function resetBoard() {
  first = null;
  second = null;
  isFirstCard = false;
  isBoardClosed = false;
}

function restartGame() {
  shuffleDeck();
}

function shuffleDeck() {
  deck.forEach((card) => {
    let randomIndex = Math.floor(Math.random() * 54);
    card.style.order = randomIndex;
  });
}

function checkGameOver() {
  if (score1 === 28) {
    alert("CONGRATULATIONS PLAYER ONE! YOU WON!");
    shuffleDeck();
    location.reload();
  } else if (score2 === 28) {
    alert("CONGRATULATIONS PLAYER TWO! YOU WON!");
    shuffleDeck();
    location.reload();
  }
}

updatePlayerTurn();
