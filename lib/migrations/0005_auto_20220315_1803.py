# Generated by Django 3.1.1 on 2022-03-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0004_account_profile_verifed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account_profile',
            name='verifed',
        ),
        migrations.AddField(
            model_name='account_profile',
            name='verification',
            field=models.CharField(default='', max_length=10),
        ),
    ]
