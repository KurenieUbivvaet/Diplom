# Generated by Django 4.2.9 on 2024-02-05 18:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Код')),
                ('valid_form', models.DateTimeField(verbose_name='Начало')),
                ('valid_to', models.DateTimeField(verbose_name='Конец')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка')),
                ('active', models.BooleanField(verbose_name='Активен')),
            ],
        ),
    ]
