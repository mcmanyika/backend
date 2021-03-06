# Generated by Django 3.1.1 on 2022-03-24 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_images')),
                ('moq', models.IntegerField()),
                ('availability', models.CharField(default='Ready to ship', max_length=20)),
                ('measurementType', models.CharField(default='Kilograms', max_length=20)),
                ('owner', models.CharField(default='', max_length=80)),
                ('status', models.CharField(default='active', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='product_images')),
                ('status', models.CharField(default='active', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('rootid', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('rate', models.IntegerField()),
                ('status', models.CharField(default='active', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('rootid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]
