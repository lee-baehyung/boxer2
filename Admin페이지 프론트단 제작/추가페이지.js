
  const products = [
    // 페이지 1
    { category: "상의", brand: "Supreme", name: "슈프림 박스로고 후드티", price: "390,000" },
    { category: "하의", brand: "DIESEL", name: "디젤 트랙 팬츠", price: "188,000" },
    { category: "신발", brand: "Nike", name: "에어포스 1", price: "137,000" },
    { category: "패션잡화", brand: "Music&Goods", name: "뽀빵이 키링", price: "29,000" },

    // 페이지 2
    { category: "상의", brand: "ADER", name: "아더에러 니트", price: "280,000" },
    { category: "하의", brand: "Musinsa", name: "테크 조거 팬츠", price: "49,000" },
    { category: "신발", brand: "Adidas", name: "이지 부스트 350", price: "299,000" },
    { category: "패션잡화", brand: "STAYC", name: "포토 키링", price: "19,000" },

    // 페이지 3
    { category: "상의", brand: "Covernat", name: "베이직 후디", price: "69,000" },
    { category: "하의", brand: "Lafudgestore", name: "테크 팬츠", price: "89,000" },
    { category: "신발", brand: "Vans", name: "올드스쿨", price: "79,000" },
    { category: "패션잡화", brand: "Hyundai", name: "현대모비스 키링", price: "9,900" }
  ];

  const itemsPerPage = 4;
  let currentPage = 1;

  function renderTable(page) {
    const start = (page - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    const tbody = document.getElementById("productTableBody");
    tbody.innerHTML = "";

    const pageData = products.slice(start, end);
    for (const item of pageData) {
      const row = `
        <tr>
          <td>${item.category}</td>
          <td>${item.brand}</td>
          <td>${item.name}</td>
          <td>${item.price}</td>
        </tr>
      `;
      tbody.innerHTML += row;
    }

    currentPage = page;
    updatePagination();
  }

  function updatePagination() {
    const buttons = document.querySelectorAll(".pagination button");
    buttons.forEach(btn => btn.classList.remove("active"));
    buttons.forEach(btn => {
      if (btn.textContent == currentPage.toString()) {
        btn.classList.add("active");
      }
    });
  }

  function goToPage(page) {
    const totalPages = Math.ceil(products.length / itemsPerPage);
    if (page < 1 || page > totalPages) return;
    renderTable(page);
  }

  // 초기 렌더링
  window.onload = () => {
    updateTime();
    setInterval(updateTime, 1000);
    renderTable(1);
  };
