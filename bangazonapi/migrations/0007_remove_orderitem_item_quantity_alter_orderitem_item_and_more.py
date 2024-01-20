# Generated by Django 4.1.3 on 2024-01-20 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0006_rename_open_order_is_open'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item_quantity',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='bangazonapi.item'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_orders', to='bangazonapi.order'),
        ),
    ]
