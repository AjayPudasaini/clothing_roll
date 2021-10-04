# Generated by Django 3.2.7 on 2021-09-27 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_image', models.ImageField(upload_to='brand/images')),
                ('brand_name', models.CharField(max_length=200)),
                ('brand_desc', models.TextField()),
                ('brand_slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='category/images')),
                ('name', models.CharField(max_length=200, null=True)),
                ('desc', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('product_name', models.CharField(max_length=500)),
                ('product_desc', models.TextField()),
                ('product_image', models.ImageField(upload_to='product/images')),
                ('display_price', models.FloatField()),
                ('actual_price', models.FloatField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothing_roll.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothing_roll.category')),
            ],
        ),
    ]