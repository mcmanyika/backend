# Generated by Django 3.1.1 on 2022-03-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0012_t_business_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_business_info',
            name='postalCode',
            field=models.IntegerField(),
        ),
    ]