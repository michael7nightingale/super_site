# Generated by Django 4.1.3 on 2023-03-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phy', '0008_remove_formula_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryphy',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
