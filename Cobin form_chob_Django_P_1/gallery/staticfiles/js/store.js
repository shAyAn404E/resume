document.addEventListener("DOMContentLoaded", function () {
  const productCards = document.querySelectorAll(".product-card");

  productCards.forEach(card => {
    card.addEventListener("contextmenu", function (e) {
      e.preventDefault(); // جلوگیری از منوی کلیک راست پیش‌فرض
      toggleDetails(card);
    });
  });

  function toggleDetails(card) {
    // بستن سایر کارت‌ها
    document.querySelectorAll(".product-card.expanded").forEach(el => {
      if (el !== card) el.classList.remove("expanded");
    });

    // باز یا بسته کردن کارت انتخاب‌شده
    card.classList.toggle("expanded");
  }
});
