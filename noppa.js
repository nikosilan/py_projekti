let balance = 0;

// ===== BACKGROUND MUSIC =====
const bgMusic = document.getElementById("bgMusic");

function playMusic() {
    if (bgMusic.paused) {
        bgMusic.volume = 0.35;
        bgMusic.play().catch(() => {});
    }
}

//  DOM ELEMENTS
const balanceDiv = document.getElementById("balance");
const computerDiv = document.getElementById("computer-roll");
const playerDiv = document.getElementById("player-roll");
const messageDiv = document.getElementById("message");

const rollBtn = document.getElementById("rollBtn");
const quitBtn = document.getElementById("quitBtn");

const dice1 = document.getElementById("dice1");
const dice2 = document.getElementById("dice2");

// Emoji for each dice number (1–6)
const diceFaces = ["⚀","⚁","⚂","⚃","⚄","⚅"];

// ===== COMPUTER DICE =====
const computerDice = [
    Math.floor(Math.random()*6) + 1,
    Math.floor(Math.random()*6) + 1
];

computerDiv.textContent = "Tietokone heitti: ? ?";

// ===== ROLL BUTTON =====
rollBtn.addEventListener("click", () => {
    playMusic(); // ensure music starts on first interaction

    messageDiv.textContent = "";

    dice1.classList.add("rolling");
    dice2.classList.add("rolling");

    let count = 0;

    const animation = setInterval(() => {
        dice1.textContent = diceFaces[Math.floor(Math.random()*6)];
        dice2.textContent = diceFaces[Math.floor(Math.random()*6)];
        count++;

        if (count > 10) {
            clearInterval(animation);

            dice1.classList.remove("rolling");
            dice2.classList.remove("rolling");

            // ===== PLAYER REAL ROLL =====
            const p1 = Math.floor(Math.random()*6) + 1;
            const p2 = Math.floor(Math.random()*6) + 1;

            dice1.textContent = diceFaces[p1 - 1];
            dice2.textContent = diceFaces[p2 - 1];

            playerDiv.textContent = `Sinun heittosi: ${p1} ja ${p2}`;

            // ===== CHECK WIN =====
            if (p1 === computerDice[0] && p2 === computerDice[1]) {
                const reward = Math.floor(Math.random()*1000) + 1;
                balance += reward;

                balanceDiv.textContent = `Saldo: ${balance}€`;
                computerDiv.textContent = `Tietokone heitti: ${computerDice[0]} ja ${computerDice[1]}`;
                messageDiv.textContent = `🎉 Onnittelut! Saat ${reward}€! 🎉`;

                rollBtn.disabled = true;
                return;
            }

            messageDiv.textContent = "❌ Ei täsmännyt, yritä uudelleen!";
        }

    }, 100);
});


// ===== QUIT BUTTON =====
quitBtn.addEventListener("click", () => {
    playMusic();
    messageDiv.textContent = `Peli päättyi. Lopullinen saldo: ${balance}€`;
    rollBtn.disabled = true;
});
