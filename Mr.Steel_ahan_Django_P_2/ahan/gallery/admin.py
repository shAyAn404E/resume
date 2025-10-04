from django.contrib import admin
from .models import GalleryImage, TrustSymbol, Logo
from django.utils.html import format_html

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)


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



@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    readonly_fields = ['image_preview']
    search_fields = ['title']
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" />'.format(obj.image.url))
        return "No Image"