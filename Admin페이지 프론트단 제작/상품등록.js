const modal = document.getElementById("productModal");
const openBtn = document.getElementById("openModal");
const closeBtn = document.querySelector(".close");

openBtn.onclick = () => {
  modal.style.display = "block";
};

closeBtn.onclick = () => {
  modal.style.display = "none";
};

window.onclick = (event) => {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

document.getElementById("registerForm").onsubmit = (e) => {
  e.preventDefault();
  const form = e.target;
  const data = {
    category: form.category.value,
    brand: form.brand.value,
    name: form.name.value,
    price: form.price.value
  };
  console.log("신규 상품 등록:", data);
  modal.style.display = "none";
};
