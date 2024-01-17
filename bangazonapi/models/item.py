from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def count(self):
        return [len(self.order_items.all())]
