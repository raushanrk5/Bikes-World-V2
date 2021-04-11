# Generated by Django 3.1.3 on 2021-04-09 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_order_invoice_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='status',
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='store.order'),
        ),
    ]
