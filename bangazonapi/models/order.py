from django.db import models
from .cashier import Cashier
from .customer import Customer

class Order(models.Model):
    cashier = models.ForeignKey(
        Cashier,
        on_delete=models.SET_NULL,
        null=True
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_DEFAULT,
        default="unknown_customer"
    )
    open_time = models.DateTimeField()
    close_time = models.DateTimeField(null=True)
    is_open = models.BooleanField()
    type = models.CharField(max_length=8)
    payment_type = models.CharField(max_length=4)
    tip_amount = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    
    def items(self):
        return [item_order.item for item_order in self.item_orders.all()]
