# Generated by Django 3.1.3 on 2021-04-03 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20210403_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
            preserve_default=False,
        ),
    ]
