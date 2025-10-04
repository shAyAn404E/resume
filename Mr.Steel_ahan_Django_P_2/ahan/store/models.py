from django.db import models


# store/models.py

class Product(models.Model):
    # ——— نام محصول ———
    name_fa        = models.CharField("نام محصول (فارسی)",    max_length=100,null=True)
    name_en        = models.CharField("Product Name (English)", max_length=100, blank=True, null=True)
    name_ar        = models.CharField("اسم المنتج (العربية)",  max_length=100, blank=True, null=True)

    # ——— توضیحات ———
    description_fa = models.TextField("توضیحات (فارسی)",null=True)
    description_en = models.TextField("Description (English)", blank=True, null=True)
    description_ar = models.TextField("الوصف (العربية)",      blank=True, null=True)

    # ——— موجودی ———
    available_fa   = models.CharField("موجودی (فارسی)",    max_length=255,null=True)
    available_en   = models.CharField("Availability (En)", max_length=255, blank=True, null=True)
    available_ar   = models.CharField("التوفر (Ar)",        max_length=255, blank=True, null=True)

    # ——— دسته‌بندی ———
    category_fa    = models.CharField("دسته‌بندی (فارسی)",   max_length=50,null=True)
    category_en    = models.CharField("Category (English)",   max_length=50, blank=True, null=True)
    category_ar    = models.CharField("فئة (العربية)",        max_length=50, blank=True, null=True)

    # ——— قیمت ———
    price_fa       = models.CharField("قیمت (فارسی)",         max_length=100,null=True)
    price_en       = models.CharField("Price (English)",      max_length=100, blank=True, null=True)
    price_ar       = models.CharField("السعر (العربية)",      max_length=100, blank=True, null=True)

    # ——— تصویر ———
    image_url      = models.CharField("آدرس عکس", max_length=255, blank=True)
    image          = models.ImageField(upload_to="products_images/", null=True, blank=True)

    # ——— وضعیت ———
    is_active      = models.BooleanField("فعّال", default=True)


    def __str__(self):
        return self.name_fa


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        #managed = False
        db_table = 'contant_messages'


class Order(models.Model):
    name = models.CharField("نام و نام خانوادگی", max_length=100)
    phone = models.CharField("شماره تماس", max_length=15)
    product_name = models.CharField("نام محصول", max_length=100)
    quantity = models.PositiveIntegerField("تعداد")
    address = models.TextField("آدرس")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product_name}"





class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    message = models.TextField(verbose_name='متن پیام')
    is_approved = models.BooleanField(default=False, verbose_name='تأیید شده')
    answer = models.TextField(blank=True, null=True, verbose_name='پاسخ مدیر')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {'✅' if self.is_approved else '⏳'}"

    #class Meta:
        #managed = False



