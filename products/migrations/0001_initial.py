# Generated by Django 3.2.9 on 2021-11-18 03:12

from django.db import migrations, models
import django.db.models.deletion
import utils.uploading


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=248)),
                ('description', models.TextField(default='Описание появится позже')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to=utils.uploading.upload_function)),
                ('description', models.TextField(default='Описание появится позже')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('characteristic', models.TextField(default='Характеристики появятся позже')),
                ('recommendation', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=utils.uploading.upload_function)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
