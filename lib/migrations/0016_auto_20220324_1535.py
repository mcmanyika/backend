# Generated by Django 3.1.1 on 2022-03-24 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0015_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='rootid',
        ),
        migrations.RemoveField(
            model_name='t_images',
            name='rootid',
        ),
        migrations.DeleteModel(
            name='contact_supplier',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='t_images',
        ),
    ]
