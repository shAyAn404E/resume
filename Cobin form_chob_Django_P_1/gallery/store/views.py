from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from .forms import ContactForm
from gallery.models import GalleryImage, TrustSymbol
from .models import Product, Message, Category, WorkSample
from django.core.paginator import Paginator

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /HandSH/",
        "Allow: /",
        "Sitemap: https://127.0.0.1:8000/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


class MessageCreateView(View):
    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')

        if name and message:
            # ایجاد پیام در دیتابیس
            Message.objects.create(name=name, message=message)

            # --- تنظیم پیام موفقیت‌آمیز ---
            messages.success(request, 'پیام شما با موفقیت دریافت و ارسال شد. متشکریم! 😊')
            # -------------------------------

        else:
            # اگر فیلدها خالی بودند، پیام خطا نمایش داده شود (اختیاری)
            messages.error(request, 'لطفاً نام و متن پیام را تکمیل کنید.')

        # ریدایرکت به صفحه اصلی (یا هر آدرس دیگری که پیام‌ها در آن نمایش داده می‌شوند)
        return redirect('store')
# در فایل store/views.py

class StoreView(View):
    def get(self, request):
        # فقط دسته‌بندی‌های فعال را دریافت می‌کنیم
        categories = Category.objects.all().order_by('name')

        # پیام‌های تأییدشده
        approved_messages = Message.objects.filter(is_approved=True).order_by('-created_at')

        # تصاویر گالری را دریافت می‌کنیم
        gallery_images = GalleryImage.objects.all()

        # نمادهای اعتماد را دریافت می‌کنیم
        trust_symbols = TrustSymbol.objects.all()

        return render(request, 'store/store.html', {
            'categories': categories,
            'approved_messages': approved_messages,
            'gallery_images': gallery_images,
            'trust_symbols': trust_symbols,
        })


class CategoryDetailView(View):
    def get(self, request, category_slug):
        try:
            category = Category.objects.get(slug=category_slug)
            all_products = category.products.filter(is_active=True)

            # --- بخش جدید برای صفحه‌بندی ---
            paginator = Paginator(all_products, 15) # 6 محصول در هر صفحه
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            # --- پایان بخش جدید ---

            # نمونه کارهای مربوط به تمام محصولات این دسته را می‌گیریم
            work_samples = WorkSample.objects.filter(product__in=all_products)

            return render(request, 'store/category_detail.html', {
                'category': category,
                'products': page_obj.object_list, # حالا از محصولات صفحه‌بندی شده استفاده می‌کنیم
                'work_samples': work_samples,
                'page_obj': page_obj, # شیء صفحه‌بندی را به قالب می‌فرستیم
            })
        except Category.DoesNotExist:
            # اگر دسته‌بندی پیدا نشد، کاربر را به صفحه اصلی برمی‌گردانیم
            return redirect('store')


class OrderView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'store/order.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ سفارش شما با موفقیت ثبت شد. با شما تماس خواهیم گرفت.")
            return redirect('order_success')
        else:
            messages.error(request, "❌ لطفاً تمام فیلدها را به‌درستی پر کنید.")
            return render(request, 'store/order.html', {'form': form})

class OrderSuccessView(View):
    def get(self, request):
        return render(request, 'store/order_success.html')

def custom_401_view(request, exception=None):
    return render(request, '401.html', status=401)

def custom_403_view(request, exception=None):
    return render(request, '403.html', status=403)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)
