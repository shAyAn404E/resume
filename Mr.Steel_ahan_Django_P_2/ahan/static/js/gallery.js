document.addEventListener('DOMContentLoaded', function () {
  // --- global lightbox (یکبار برای همه گالری‌ها) ---
  const globalLightbox = document.getElementById('lightbox');
  const globalLightboxImage = document.getElementById('lightbox-image');

  function openLightbox(url) {
    if (!globalLightbox || !globalLightboxImage) return;
    globalLightboxImage.src = url;
    globalLightbox.style.display = 'flex';
    globalLightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (!globalLightbox) return;
    globalLightbox.style.display = 'none';
    globalLightbox.classList.remove('open');
    if (globalLightboxImage) globalLightboxImage.src = '';
    document.body.style.overflow = 'auto';
  }

  if (globalLightbox) {
    globalLightbox.addEventListener('click', closeLightbox);
    if (globalLightboxImage) {
      globalLightboxImage.addEventListener('click', function (e) { e.stopPropagation(); });
    }
  }

  // --- برای هر gallery-wrapper یک تنظیم جدا بزن ---
  const wrappers = document.querySelectorAll('.gallery-wrapper');
  wrappers.forEach(wrapper => {
    const gallery = wrapper.querySelector('.work-samples-grid');
    if (!gallery) return;

    // دکمه‌ها: اگر خواستی صریح کلاس بذاری بهتره (nav-button-left / nav-button-right)
    const navButtons = wrapper.querySelectorAll('.nav-button');
    const leftButton = wrapper.querySelector('.nav-button-left') || navButtons[0] || null;
    const rightButton = wrapper.querySelector('.nav-button-right') || navButtons[1] || null;
    const items = gallery.querySelectorAll('.work-sample-item');
    if (!items || items.length === 0) return;

    // gap خواندن از CSS (fallback به 24px)
    const galleryStyle = window.getComputedStyle(gallery);
    let gapVal = galleryStyle.getPropertyValue('gap') || galleryStyle.getPropertyValue('column-gap') || '24px';
    gapVal = gapVal.trim();
    const gapNum = parseFloat(gapVal) || 24;

    // محاسبه عرض آیتم (به‌روز می‌شود در resize یا بعد از لود تصاویر)
    let itemWidth = items[0].getBoundingClientRect().width + gapNum;
    function recalcItemWidth() {
      if (items.length > 0) itemWidth = items[0].getBoundingClientRect().width + gapNum;
    }
    window.addEventListener('resize', recalcItemWidth);
    // اگر تصاویر دیر لود میشن، بعد از load دوباره محاسبه کن
    items.forEach(it => {
      const img = it.querySelector('img');
      if (img && !img.complete) {
        img.addEventListener('load', () => setTimeout(recalcItemWidth, 50));
      }
    });
    recalcItemWidth();

    let autoScrollInterval = null;
    function ensureLoopAfterScroll(timeout = 500) {
      clearTimeout(wrapper._galleryLoopTimeout);
      wrapper._galleryLoopTimeout = setTimeout(() => {
        const atEnd = gallery.scrollLeft + gallery.clientWidth >= gallery.scrollWidth - 2;
        const atStart = gallery.scrollLeft <= 5;
        if (atEnd) {
          gallery.scrollTo({ left: 0, behavior: 'smooth' });
        } else if (atStart) {
          const maxLeft = Math.max(0, gallery.scrollWidth - gallery.clientWidth);
          gallery.scrollTo({ left: maxLeft, behavior: 'auto' });
        }
      }, timeout);
    }




    // می‌تونی جهت و اینتروال رو با data-attributes تنظیم کنی:
    // <div class="gallery-wrapper" data-direction="right" data-interval="3000">
    const direction = (wrapper.dataset.direction || 'right').toLowerCase(); // 'left' یا 'right'
    const intervalMs = parseInt(wrapper.dataset.interval) || 3000;

    function startAutoScroll() {
    if (!autoScrollInterval) {
        autoScrollInterval = setInterval(() => {
            const atEnd = gallery.scrollLeft + gallery.clientWidth >= gallery.scrollWidth - 2;

            if (atEnd) {
                // وقتی رسید ته، برگرد به اول
                gallery.scrollTo({ left: 0, behavior: 'auto' });
            } else {
                // ادامه بده تا ته
                gallery.scrollBy({ left: -itemWidth, behavior: 'smooth' });
            }
        }, 2000); // هر ۳ ثانیه حرکت کنه
    }
}


    function stopAutoScroll() {
      clearInterval(autoScrollInterval);
      autoScrollInterval = null;
      clearTimeout(wrapper._galleryLoopTimeout);
    }

    // IntersectionObserver برای شروع/توقف خودکار وقتی داخل viewport باشه
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) startAutoScroll();
        else stopAutoScroll();
      });
    }, { threshold: 0.5 });
    io.observe(gallery);

// --- دکمه‌ها (اصلاح‌شده برای حرکت تک واحدی بدون لوپ ناخواسته) ---
    if (rightButton) {
      rightButton.addEventListener('click', () => {
        stopAutoScroll();
        // حرکت به سمت چپ (جلو رفتن در لیست در گالری‌های RTL)
        // جهت منفی در scrollBy به معنای رفتن به سمت چپ در DOM است.
        gallery.scrollBy({ left: itemWidth, behavior: 'smooth' });
        // ensureLoopAfterScroll(); <-- این خط را حذف کنید
      });
    }

    if (leftButton) {
      leftButton.addEventListener('click', () => {
        stopAutoScroll();
        // حرکت به سمت راست (عقب رفتن در لیست در گالری‌های RTL)
        // جهت مثبت در scrollBy به معنای رفتن به سمت راست در DOM است.
        gallery.scrollBy({ left: -itemWidth, behavior: 'smooth' });
        // ensureLoopAfterScroll(); <-- این خط را حذف کنید
      });
    }

    // ... بقیه کد ...

    // توقف/شروع خودکار روی هاور (موبایل از این استفاده نمیکنه ولی مشکلی نیست)
    gallery.addEventListener('mouseenter', stopAutoScroll);
    gallery.addEventListener('mouseleave', startAutoScroll);

    // lightbox برای آیتم‌ها
    items.forEach(item => {
      item.addEventListener('click', function (e) {
        e.preventDefault();
        // data-src یا data-img-url یا تصویر داخلی
        const src = item.dataset.src || item.dataset.imgUrl || item.getAttribute('href') || (item.querySelector('img') && item.querySelector('img').src);
        if (src) openLightbox(src);
      });
    });

    // استارت اولیه (اگر داخل viewport بود observer خودش استارت میکنه)
    // ولی اگر خواستی فوراً استارت شه، uncomment کن:
    // startAutoScroll();
  }); // end wrappers.forEach
});
