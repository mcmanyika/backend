# Generated by Django 3.1.1 on 2022-01-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0018_auto_20220125_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_images',
            name='img',
            field=models.ImageField(upload_to='product_images'),
        ),
    ]