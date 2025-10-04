from django.db import models
from ckeditor.fields import RichTextField

# --- مدل جدید برای دسته‌بندی‌ها ---
class Category(models.Model):
    name = models.CharField("نام دسته‌بندی", max_length=200, db_index=True)
    slug = models.SlugField("اسلاگ", max_length=200, unique=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    content = RichTextField(verbose_name="محتوای توضیحات")

    class Meta:
        ordering = ('name',)
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته‌بندی‌ها محصول'

    def __str__(self):
        return self.name


# --- مدل Product (اصلاح شده) ---
class Product(models.Model):
    name = models.CharField("نام محصول", max_length=100, null=True)
    description = models.TextField("توضیحات", null=True)

    # --- فیلد دسته‌بندی به ForeignKey تغییر یافت ---
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="دسته‌بندی" ,null=True )


    image_url = models.CharField("آدرس عکس", max_length=255, blank=True)
    image = models.ImageField(upload_to="products_images/", null=True, blank=True)
    is_active = models.BooleanField("فعّال", default=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name


# --- مدل جدید برای نمونه کارها ---
class WorkSample(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='work_samples',
        on_delete=models.CASCADE,
        verbose_name='محصول',
        help_text='این نمونه کار مربوط به کدام محصول است؟'
    )
    image = models.ImageField(
        upload_to='work_samples/%Y/%m/%d/',
        verbose_name='عکس',
        help_text='عکس نمونه کار را آپلود کنید.'
    )
    description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='توضیحات',
        help_text='توضیحات کوتاه برای نمونه کار (اختیاری).'
    )

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کارها'

    def __str__(self):
        return f"نمونه کار برای {self.product.name}"



class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=150, verbose_name='ایمیل')
    phone = models.CharField(max_length=20, verbose_name='شماره تماس')
    message = models.TextField(verbose_name='متن سفارش')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ و زمان')

    class Meta:
        verbose_name = 'سفارش ثبت شده'
        verbose_name_plural = 'سفارشات ثبت شده'
        ordering = ['-created_at']

    def __str__(self):
        return f"سفارش از {self.full_name}"


class Message(models.Model):
    # ... کدهای فعلی شما ...
    name = models.CharField(max_length=100, verbose_name='نام')
    message = models.TextField(verbose_name='متن پیام')
    is_approved = models.BooleanField(default=False, verbose_name='تأیید شده')
    answer = models.TextField(blank=True, null=True, verbose_name='پاسخ مدیر')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {'✅' if self.is_approved else '⏳'}"

    class Meta:
        verbose_name = 'سوالات متداول'
        verbose_name_plural = 'سوالات متداول'