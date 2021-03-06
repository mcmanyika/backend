# Generated by Django 3.1.1 on 2022-03-15 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0005_auto_20220315_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='accnt_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('mobile', models.CharField(default='', max_length=25)),
                ('email', models.EmailField(default='', max_length=254)),
                ('owner', models.CharField(default='', max_length=80)),
                ('verification', models.CharField(default='not verified', max_length=20)),
                ('status', models.CharField(default='active', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
