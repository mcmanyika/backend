# Generated by Django 3.1.1 on 2022-01-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0011_auto_20220120_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='moq',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
