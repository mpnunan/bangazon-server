# Generated by Django 4.1.3 on 2024-01-09 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='descriptoin',
            new_name='description',
        ),
    ]
