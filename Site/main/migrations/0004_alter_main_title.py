# Generated by Django 4.1.3 on 2023-01-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_main_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Заголовок'),
        ),
    ]
