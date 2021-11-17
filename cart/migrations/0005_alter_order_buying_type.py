# Generated by Django 3.2.9 on 2021-11-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20211117_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('self', 'Pickup'), ('delivery', 'Delivery')], max_length=100, verbose_name='Тип заказа'),
        ),
    ]