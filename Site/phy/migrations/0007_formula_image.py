# Generated by Django 4.1.3 on 2023-02-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phy', '0006_formula_formula_formula_lined_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula',
            name='image',
            field=models.ImageField(null=True, upload_to='formulas_images/', verbose_name='Изображение'),
        ),
    ]