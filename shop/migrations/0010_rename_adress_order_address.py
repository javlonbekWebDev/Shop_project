# Generated by Django 4.0.5 on 2022-08-13 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_orderproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adress',
            new_name='address',
        ),
    ]