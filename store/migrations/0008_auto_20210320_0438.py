# Generated by Django 3.1.3 on 2021-03-20 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20201115_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default=True, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default=True, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default=True, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default=True, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='mob_no',
            field=models.CharField(default=True, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shop_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='zip_code',
            field=models.CharField(default=True, editable=False, max_length=10),
            preserve_default=False,
        ),
    ]
