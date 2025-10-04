from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from .models import Product, Message
from .forms import ContactForm
from gallery.models import GalleryImage

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
            Message.objects.create(name=name, message=message)
        return redirect('store')

class StoreView(View):
    def get(self, request):
        # فقط محصولات فعال
        products = Product.objects.filter(is_active=True)

        # تعیین زبان جاری
        lang = request.LANGUAGE_CODE  # 'fa', 'en' یا 'ar'
        suffix = lang if lang in ('fa', 'en', 'ar') else 'fa'

        # می‌سازیم دیکشنری دسته‌بندی → لیست محصولات
        categories = {}
        for p in products:
            cat = getattr(p, f'category_{suffix}') or p.category_fa
            categories.setdefault(cat, []).append(p)

        # آماده‌سازی لیست قابل پیمایش
        category_list = [
            {'name': cat, 'products': plist}
            for cat, plist in categories.items()
        ]

        # پیام‌های تأییدشده
        approved_messages = Message.objects.filter(is_approved=True).order_by('-created_at')

        # عکس هایه گالری
        gallery_images = GalleryImage.objects.all()

        return render(request, 'store/store.html', {
            'categories': category_list,
            'approved_messages': approved_messages,
            'gallery_images': gallery_images,
        })

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
