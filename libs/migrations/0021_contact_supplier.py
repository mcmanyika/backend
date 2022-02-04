# Generated by Django 3.1.1 on 2022-01-26 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0020_products_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=800)),
                ('quantity', models.IntegerField()),
                ('owner', models.CharField(default='0xF0bA39D4eC7B977e6A47aA00165020C1DFD15226', max_length=80)),
                ('status', models.CharField(default='active', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('rootid', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='libs.products')),
            ],
        ),
    ]
