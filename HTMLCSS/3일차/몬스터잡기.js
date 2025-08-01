let playerHP = 100;
let monsterHP = 100;
let isPlayerTurn = true;
let level = 1;
let maxPlayerHP = 100;

function updateStatus() {
  document.getElementById("player-hp-text").innerText = `${playerHP}/${maxPlayerHP}`;
  document.getElementById("monster-hp-text").innerText = `${monsterHP}/100`;
  document.getElementById("player-hp").style.width = (playerHP / maxPlayerHP) * 100 + "%";
  document.getElementById("monster-hp").style.width = monsterHP + "%";
  document.getElementById("level").innerText = level;
}

function playSound(id) {
  const sound = document.getElementById(id);
  if (sound) {
    sound.currentTime = 0;
    sound.play();
  }
}

function endGame(winner) {
  const log = document.getElementById("log");
  document.getElementById("attack-btn").disabled = true;

  if (winner === "player") {
    playSound("victory-sound");
    log.innerText = "🎉 승리! 몬스터를 처치했습니다!\n레벨이 올라갑니다!";
    level++;
    maxPlayerHP += 20;
    playerHP = maxPlayerHP;
    monsterHP = 100;

    // 다음 레벨로 자동 재시작 (약간의 텀)
    setTimeout(() => {
      document.getElementById("attack-btn").disabled = false;
      isPlayerTurn = true;
      updateStatus();
      log.innerText = `🆙 Lv.${level} 몬스터 출현!`;
    }, 2000);
  } else {
    playSound("defeat-sound");
    log.innerText = "💀 패배... 플레이어가 쓰러졌습니다.";
  }
}

function monsterCounter() {
  const damage = Math.floor(Math.random() * 11) + 5; // 5~15
  playerHP -= damage;
  if (playerHP < 0) playerHP = 0;

  playSound("hit-sound");
  updateStatus();

  const log = document.getElementById("log");
  log.innerText = `👾 몬스터가 반격하여 ${damage}의 피해를 주었습니다!`;

  if (playerHP <= 0) {
    endGame("monster");
  } else {
    isPlayerTurn = true;
    document.getElementById("attack-btn").disabled = false;
  }
}

function playerAttack() {
  if (!isPlayerTurn) return;

  const damage = Math.floor(Math.random() * 16 + 10 + level * 2); // 레벨이 높을수록 강해짐
  monsterHP -= damage;
  if (monsterHP < 0) monsterHP = 0;

  playSound("attack-sound");
  updateStatus();

  const log = document.getElementById("log");
  log.innerText = `🧙‍♂️ 플레이어가 ${damage}의 피해를 주었습니다!`;

  isPlayerTurn = false;
  document.getElementById("attack-btn").disabled = true;

  if (monsterHP <= 0) {
    endGame("player");
  } else {
    setTimeout(monsterCounter, 1000);
  }
}

// 초기화
updateStatus();


