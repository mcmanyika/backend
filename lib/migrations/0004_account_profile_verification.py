# Generated by Django 3.1.1 on 2022-03-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0003_auto_20220308_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_profile',
            name='verification',
            field=models.CharField(default='', max_length=10),
        ),
    ]
