# Generated by Django 4.1.3 on 2023-02-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phy', '0004_alter_categoryphy_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name='Название отображения'),
        ),
        migrations.AlterField(
            model_name='formula',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название обращения'),
        ),
    ]