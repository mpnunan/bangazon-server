# Generated by Django 4.1.3 on 2024-01-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0002_rename_descriptoin_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='close_time',
            field=models.DateTimeField(null=True),
        ),
    ]