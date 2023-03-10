from django.db import models


class Main(models.Model):
    title = models.CharField(null=True, max_length=100, verbose_name='Заголовок', )
    content = models.TextField(null=True, blank=True, verbose_name='Текст', )
    image = models.ImageField(upload_to='photos/', null=True, verbose_name='Изображение', )
    exist = models.BooleanField(default=True, verbose_name='Существует', )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главная Страница'
        verbose_name_plural = 'Главная Страница'

