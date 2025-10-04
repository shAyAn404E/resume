from django.contrib import admin
import jdatetime
from .models import Product, ContactMessage, Message, Category, WorkSample
from django.utils.html import format_html


# ثبت مدل Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    fields = ['name', 'slug', 'image', 'content']
    prepopulated_fields = {'slug': ('name',)}


# ثبت مدل Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'category']  # category در لیست نمایش داده شود
    search_fields = ['name']
    list_filter = ['is_active', 'category']
    readonly_fields = ['image_url']

    # --- از fieldsets حذف کرده و از fields استفاده می‌کنیم ---
    fields = (
        'name',
        'category',  # <--- فیلد category باید حتما اینجا باشد
        'description',
        'image',
        'image_url',
        'is_active',
    )


# ثبت مدل Message
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_message', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['name', 'message']
    readonly_fields = ['name', 'message', 'created_at']

    def short_message(self, obj):
        return obj.message[:40] + "..." if len(obj.message) > 40 else obj.message

    short_message.short_description = 'متن پیام'

    fieldsets = (
        ('مشخصات پیام', {
            'fields': ('name', 'message', 'created_at')
        }),
        ('مدیریت', {
            'fields': ('is_approved', 'answer')
        }),
    )


# ثبت مدل WorkSample
@admin.register(WorkSample)
class WorkSampleAdmin(admin.ModelAdmin):
    list_display = ['image', 'product']
    list_filter = ['product']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />'.format(obj.image.url))
        return "No Image"

    image_preview.short_description = 'پیش‌نمایش تصویر'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # فیلدهای نمایش داده شده در لیست سفارشات
    list_display = ['full_name', 'phone', 'jalali_created_at']
    search_fields = ['full_name', 'phone', 'message']

    # فیلدهای غیر قابل ویرایش در فرم ویرایش
    readonly_fields = ['full_name', 'email', 'phone', 'message', 'created_at']

    # فیلترها
    list_filter = ['created_at']

    # متد جدید برای تبدیل تاریخ میلادی به شمسی
    def jalali_created_at(self, obj):
        if obj.created_at:
            jdate = jdatetime.datetime.fromgregorian(datetime=obj.created_at)
            return jdate.strftime('%Y/%m/%d - %H:%M')
        return None

    jalali_created_at.short_description = ' و زمان ثبت'

