# Generated by Django 3.1.3 on 2021-04-04 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20210404_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=True),
            preserve_default=False,
        ),
    ]