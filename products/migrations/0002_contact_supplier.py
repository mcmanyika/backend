# Generated by Django 3.1.1 on 2022-03-24 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=800)),
                ('quantity', models.IntegerField()),
                ('client', models.CharField(default='', max_length=80)),
                ('owner', models.CharField(default='', max_length=80)),
                ('status', models.CharField(default='active', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('rootid', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]