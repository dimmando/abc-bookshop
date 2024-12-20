# Generated by Django 4.2.16 on 2024-10-31 11:26

import cloudinary.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ean', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('ISBN', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('title', models.CharField(max_length=254)),
                ('author', models.CharField(max_length=254)),
                ('size', models.CharField(blank=True, max_length=254, null=True)),
                ('number_of_pages', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='', max_length=1024, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0, message=None)])),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0, message=None)])),
                ('new_arrival', models.BooleanField(blank=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('is_sale', models.BooleanField()),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0, message=None)])),
                ('by_age', models.CharField(choices=[('schoolchildren', 'schoolchildren'), ('students', 'students'), ('professionals', 'professionals')], max_length=40)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
