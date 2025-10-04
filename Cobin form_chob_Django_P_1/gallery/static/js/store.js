document.addEventListener("DOMContentLoaded", function () {
    const productCards = document.querySelectorAll(".product-card");
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.getElementById('lightbox-image');

    // --- توابع Lightbox (داخلی) ---

    // تابع بستن Lightbox
    function closeLightbox() {
        if (lightbox) {
            lightbox.style.display = 'none'; // مخفی کردن Lightbox
            document.body.style.overflow = 'auto'; // بازگرداندن اسکرول
        }
    }

    // تابع باز کردن Lightbox
    function openProductLightbox(event, element) {
        // جلوگیری از رفتار پیش‌فرض لینک (که شما را به بالا می‌برد)
        event.preventDefault();

        // گرفتن آدرس عکس از صفت داده (data-img-url)
        const imageUrl = element.getAttribute('data-img-url');

        if (imageUrl && lightbox && lightboxImage) {
            lightboxImage.src = imageUrl;
            lightbox.style.display = 'flex'; // نمایش Lightbox
            document.body.style.overflow = 'hidden'; // جلوگیری از اسکرول صفحه زیرین
        }
    }

    // --- تابع toggleDetails (برای کلیک راست) ---
    function toggleDetails(card) {
        // بستن سایر کارت‌ها
        document.querySelectorAll(".product-card.expanded").forEach(el => {
            if (el !== card) el.classList.remove("expanded");
        });

        // باز یا بسته کردن کارت انتخاب‌شده
        card.classList.toggle("expanded");
    }

    // --- Listenerها برای کارت‌های محصول ---
    productCards.forEach(card => {
        // 1. کلیک راست (contextmenu) برای toggleDetails
        card.addEventListener("contextmenu", function (e) {
            e.preventDefault();
            toggleDetails(card);
        });

        // 2. کلیک چپ (click) برای Lightbox
        card.addEventListener("click", function (e) {
            openProductLightbox(e, card);
        });
    });

    // --- Listener برای بستن Lightbox ---
    if (lightbox) {
        // Listener کلیک روی پس‌زمینه Lightbox برای بستن
        lightbox.addEventListener('click', closeLightbox);

        // جلوگیری از بسته شدن با کلیک روی خود عکس
        if (lightboxImage) {
            lightboxImage.addEventListener('click', function(e) {
                e.stopPropagation();
            });
        }
    }

});