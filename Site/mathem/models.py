from django.db import models


class CategoryMathem(models.Model):
    category_name = models.CharField(max_length=100, db_index=True, null=True, verbose_name='Название категории', )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Mathem(models.Model):
    title = models.CharField(max_length=100,  verbose_name='Заголовок', )
    content = models.TextField(blank=True, verbose_name='Текст', )
    image = models.ImageField(upload_to='photos/', null=True, verbose_name='Изображение', )
    exist = models.BooleanField(default=True, verbose_name='Существует', )
    cat = models.ForeignKey(CategoryMathem, null=True, on_delete=models.PROTECT, verbose_name='Категория', )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Математика'
        verbose_name_plural = 'Математика'

