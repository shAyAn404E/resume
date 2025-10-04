document.addEventListener("DOMContentLoaded", function () {
    const productCards = document.querySelectorAll(".product-card");
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.getElementById('lightbox-image');

    productCards.forEach(card => {
        card.addEventListener("click", function (e) {
            e.preventDefault();
            const imageUrl = card.getAttribute("data-img-url");
            lightboxImage.src = imageUrl;
            lightbox.style.display = "flex";
            document.body.style.overflow = "hidden";
        });
    });

    lightbox.addEventListener("click", function () {
        lightbox.style.display = "none";
        document.body.style.overflow = "auto";
    });
});
