# Generated by Django 3.1.3 on 2021-04-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_auto_20210404_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoice_id',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
