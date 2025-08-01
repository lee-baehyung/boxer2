const form = document.getElementById("form");

form.addEventListener("submit", function(event) {
  event.preventDefault(); // 기존 기능 차단

  let userID = event.target.id.value;
  let userPw1 = event.target.pw1.value;
  let userPw2 = event.target.pw2.value; // 오타 수정
  let userName = event.target.name.value;
  let userPhone = event.target.phone.value;
  let userPosition = event.target.position.value;
  let userGender = event.target.gender.value;
  let userEmail = event.target.email.value;
  let userIntro = event.target.intro.value;

  if (userID.length < 6) {
    alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요.");
    return;
  }

  if (userPw1 !== userPw2) {
    alert("비밀번호가 일치하지 않습니다.");
    return;
  }

  // 환영 인사
  document.body.innerHTML = ""; // 기존 내용 삭제
  document.write(`<p>${userID}님을 환영합니다</p>`); // 템플릿 리터럴로 수정
});
