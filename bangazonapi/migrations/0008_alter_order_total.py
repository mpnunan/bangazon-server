# Generated by Django 4.1.3 on 2024-01-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0007_remove_orderitem_item_quantity_alter_orderitem_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]