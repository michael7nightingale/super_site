# Generated by Django 4.1.3 on 2023-01-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymathem',
            name='category_name',
            field=models.CharField(db_index=True, max_length=100, null=True, verbose_name='Название категории'),
        ),
        migrations.AddField(
            model_name='mathem',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='mathem',
            name='exist',
            field=models.BooleanField(default=True, verbose_name='Существует'),
        ),
        migrations.AddField(
            model_name='mathem',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/', verbose_name='Изображение'),
        ),
    ]
