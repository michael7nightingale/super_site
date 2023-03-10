from django.db import models
from django.urls import reverse


class CategoryPhy(models.Model):
    category_name = models.CharField(max_length=100, db_index=True, null=True, verbose_name='Название раздела', )
    slug = models.SlugField(db_index=True, null=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category_physics', kwargs={"cat_slug": self.slug})

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Phy(models.Model):
    title = models.CharField(max_length=100,  verbose_name='Заголовок', )
    content = models.TextField(blank=True, verbose_name='Текст', )
    image = models.ImageField(upload_to='photos/', verbose_name='Изображение', null=True, blank=True, )
    exist = models.BooleanField(default=True, verbose_name='Существует', )
    cat = models.ForeignKey(CategoryPhy, null=True, on_delete=models.PROTECT, verbose_name='Раздел', )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Физика'
        verbose_name_plural = 'Физика'


class Formula(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название обращения")
    title = models.CharField(max_length=200, verbose_name="Название отображения", null=True)
    content = models.TextField(blank=True, verbose_name="Описание")
    cat = models.ForeignKey("CategoryPhy", null=True, on_delete=models.PROTECT, verbose_name="Раздел")
    # image = models.ImageField(upload_to='formulas_images/', verbose_name='Изображение', null=True,)
    formula = models.CharField(max_length=100, verbose_name='Формула', null=True)
    template_name = models.CharField(max_length=100, verbose_name='Имя шаблона', null=True)
    lined_type = models.CharField(max_length=100, verbose_name='Линейный тип', null=True)
    slug = models.SlugField(db_index=True, null=True, unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Формула'
        verbose_name_plural = 'Формулы'

