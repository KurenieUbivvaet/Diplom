# Generated by Django 4.2.9 on 2024-02-06 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'ordering': ('code',), 'verbose_name': 'Купон', 'verbose_name_plural': 'Купоны'},
        ),
        migrations.AlterModelTable(
            name='coupon',
            table='Купоны',
        ),
    ]