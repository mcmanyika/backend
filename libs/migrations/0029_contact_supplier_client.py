# Generated by Django 3.2.5 on 2022-02-15 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0028_remove_contact_supplier_enquirer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_supplier',
            name='client',
            field=models.CharField(default='', max_length=80),
        ),
    ]