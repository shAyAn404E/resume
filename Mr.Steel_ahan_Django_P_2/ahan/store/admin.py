from django.contrib import admin
from .models import Product, ContactMessage,Message


admin.site.register(ContactMessage)




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_fa', 'price_fa', 'available_fa', 'is_active']
    search_fields = ['name_fa', 'name_en', 'name_ar']
    list_filter = ['is_active', 'category_fa']
    readonly_fields = ['image_url']

    fieldsets = (
        ('نام‌ها', {
            'fields': ('name_fa', 'name_en', 'name_ar')
        }),
        ('توضیحات', {
            'fields': ('description_fa', 'description_en', 'description_ar')
        }),
        ('موجودی و دسته‌بندی', {
            'fields': ('available_fa', 'available_en', 'available_ar',
                       'category_fa', 'category_en', 'category_ar')
        }),
        ('قیمت‌گذاری', {
            'fields': ('price_fa', 'price_en', 'price_ar')
        }),
        ('تصویر', {
            'fields': ('image', 'image_url')
        }),
        ('وضعیت', {
            'fields': ('is_active',)
        }),
    )



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