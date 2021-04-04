# Generated by Django 3.1.3 on 2021-03-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_category_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(default=1, max_length=100, unique=True),
        ),
    ]