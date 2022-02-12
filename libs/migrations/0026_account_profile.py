# Generated by Django 3.1.1 on 2022-02-12 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0025_auto_20220207_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='account_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('owner', models.CharField(default='', max_length=80)),
                ('status', models.CharField(default='active', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]