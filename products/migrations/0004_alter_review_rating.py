# Generated by Django 3.2.9 on 2021-11-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.SmallIntegerField(),
        ),
    ]