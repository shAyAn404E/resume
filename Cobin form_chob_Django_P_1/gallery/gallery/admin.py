from django.contrib import admin
from .models import GalleryImage, TrustSymbol
from django.utils.html import format_html


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    # این کد تصویر، عنوان و زمان آپلود را نمایش می‌دهد
    list_display = ['title', 'uploaded_at', 'image_preview']
    search_fields = ['title']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />'.format(obj.image.url))
        return "No Image"

    image_preview.short_description = 'پیش‌نمایش تصویر'



# کلاس ادمین برای نمادهای اعتماد
@admin.register(TrustSymbol)
class TrustSymbolAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview']
    readonly_fields = ['image_preview']
    search_fields = ['title']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />'.format(obj.image.url))
        return "No Image"

    image_preview.short_description = 'پیش‌نمایش تصویر'