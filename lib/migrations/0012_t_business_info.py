# Generated by Django 3.1.1 on 2022-03-21 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0011_auto_20220316_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_business_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(default='', max_length=50)),
                ('address1', models.CharField(default='', max_length=50)),
                ('address2', models.CharField(default='', max_length=50)),
                ('postalCode', models.IntegerField(default='', max_length=10)),
                ('city', models.CharField(default='', max_length=30)),
                ('country', models.CharField(default='Zimbabwe', max_length=50)),
                ('companyOwner', models.CharField(default='', max_length=50)),
                ('dob', models.CharField(default='', max_length=10)),
                ('idType', models.CharField(default='', max_length=20)),
                ('idCard', models.ImageField(upload_to='business_docs')),
                ('numberOfEmployees', models.CharField(default='', max_length=50)),
                ('registrationNumber', models.CharField(default='', max_length=20)),
                ('regCertificate', models.ImageField(upload_to='business_docs')),
                ('status', models.CharField(default='active', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('rootid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lib.account_profile')),
            ],
        ),
    ]