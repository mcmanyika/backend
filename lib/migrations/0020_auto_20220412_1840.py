# Generated by Django 3.1.1 on 2022-04-12 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0019_remove_t_business_info_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_business_info',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='t_business_info',
            name='mobile',
            field=models.CharField(default='', max_length=25),
        )
    ]