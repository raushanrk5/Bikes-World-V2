# Generated by Django 3.1.3 on 2021-04-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_order_orderproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='mob_no',
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
