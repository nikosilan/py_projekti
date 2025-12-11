
if (response.open_file) {
    window.open(response.open_file, "_blank");
}


let balance = 0;
let gameOver = false;

// ===== BACKGROUND MUSIC =====
const bgMusic = document.getElementById("bgMusic");

function playMusic() {
    if (bgMusic.paused) {
        bgMusic.volume = 0.35;
        bgMusic.play().catch(() => {});
    }
}

// ===== DOM ELEMENTS =====
const balanceDiv = document.getElementById("balance");
const computerDiv = document.getElementById("computer-roll");
const playerDiv = document.getElementById("player-roll");
const messageDiv = document.getElementById("message");
const rollBtn = document.getElementById("rollBtn");
const quitBtn = document.getElementById("quitBtn");
const dice1 = document.getElementById("dice1");
const dice2 = document.getElementById("dice2");

// ORIGINAL NOPPA EMOJIS in an array
const diceFaces = ["⚀","⚁","⚂","⚃","⚄","⚅"];

// ===== INITIAL SETUP (computer rolls FRESH every player roll!) =====
computerDiv.textContent = "";


// ===== ROLL FUNCTION (computer rolls uuden nopan each time!) =====
function rollDice() {
    if (gameOver || rollBtn.disabled) return;

    playMusic();
    messageDiv.textContent = "";
    messageDiv.style.color = "";
    messageDiv.style.fontSize = "";

    rollBtn.disabled = true;  // Prevent spam

    // ===== STEP 1: Computer rolls  (new every time!) =====
    const computerDice = [
        Math.floor(Math.random() * 6) + 1,
        Math.floor(Math.random() * 6) + 1
    ];
    const computerSum = computerDice[0] + computerDice[1];

    let count = 0;
    const animation = setInterval(() => {
        // Shaking animation (player dice only)
        dice1.textContent = diceFaces[Math.floor(Math.random() * 6)];
        dice2.textContent = diceFaces[Math.floor(Math.random() * 6)];
        count++;

        if (count > 15) {  // Longer suspense !
            clearInterval(animation);

            // ===== STEP 2: paljastaan PLAYER roll =====
            const p1 = Math.floor(Math.random() * 6) + 1;
            const p2 = Math.floor(Math.random() * 6) + 1;
            const playerSum = p1 + p2;

            dice1.textContent = diceFaces[p1 - 1];
            dice2.textContent = diceFaces[p2 - 1];
            playerDiv.textContent = `Sinun heittosi: ${p1} ja ${p2} (summa: ${playerSum})`;

            // ===== STEP 3: paljastaan tietokoneen roll (suspense!) =====
            computerDiv.textContent = `Tietokone heitti: ${computerDice[0]} ja ${computerDice[1]} (summa: ${computerSum})`;

            // ===== WIN: jos tietokoneen ja pelajaan heittöjen summat täsmasivät !  =====
          if (playerSum === computerSum) {
    const reward = Math.floor(Math.random() * 400) + 100;  // 100-500€
    balance += reward;
    balanceDiv.textContent = `Saldo: ${balance}€`;

    // ===== SEND TO BACKEND =====
    fetch("http://localhost:5000/api/save-prize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            player_name: "Player1",
            prize: reward
        })
    })
    .then(res => res.json())
    .then(data => console.log(data.message))
    .catch(err => console.error(err));

    messageDiv.textContent = `🎉 ONNITTELUT! Summat täsmäsivät (${computerSum}) — saat ${reward}€! 🎉`;
    messageDiv.style.color = "gold";
    messageDiv.style.fontSize = "1.8em";
    messageDiv.style.fontWeight = "bold";

    gameOver = true;
    rollBtn.style.opacity = "0.4";
    rollBtn.style.cursor = "not-allowed";

    setTimeout(() => {
        window.location.href = "index.html";
    }, 4000);
}
 else {
                messageDiv.textContent = `❌ Summat eivät täsmänneet (${playerSum} vs ${computerSum}) — yritä uudelleen!`;
                messageDiv.style.color = "#ff4444";
                rollBtn.disabled = false;  // Ready for next round
            }
        }
    }, 80);  // Fast shake for tension
}

// ===== BUTTONS =====
rollBtn.addEventListener("click", rollDice);

quitBtn.addEventListener("click", () => {
    if (gameOver) return;

    playMusic();
    gameOver = true;
    rollBtn.disabled = true;
    rollBtn.style.opacity = "0.4";
    rollBtn.style.cursor = "not-allowed";

    messageDiv.textContent = `Peli päättyi. Lopullinen saldo: ${balance}€`;
    messageDiv.style.color = "#000";

    setTimeout(() => {
        window.location.href = "index.html";
    }, 2500);
});
