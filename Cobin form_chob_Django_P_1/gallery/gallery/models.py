from django.db import models

class GalleryImage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='عنوان عکس')
    image = models.ImageField(upload_to='gallery/', verbose_name='تصویر')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'تصاویر گالری'
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title if self.title else f'عکس گالری {self.id}'


# gallery/models.py

from django.db import models


class GalleryImage(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان عکس")
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "تصویر گالری"
        verbose_name_plural = "تصاویر گالری"

    def __str__(self):
        return self.title


# مدل جدید برای نمادهای اعتماد
class TrustSymbol(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان نماد")
    image = models.ImageField(upload_to='trust_symbols/', verbose_name="تصویر نماد")

    class Meta:
        verbose_name = "نماد اعتماد"
        verbose_name_plural = "نمادهای اعتماد"

    def __str__(self):
        return self.title