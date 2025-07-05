from datetime import date, timedelta
from django.db import models
# Create your models here.

class Medicine(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    category=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    low_stock_threshold = models.PositiveIntegerField(default=10)
    updated_at = models.DateTimeField(auto_now=True)

    def total_quantity(self):
        return sum(batch.quantity for batch in self.batches.all())

    def is_low_stock(self):
        return self.total_quantity() < self.low_stock_threshold

    def __str__(self):
        return self.name


class Batch(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='batches')
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField()
    received_date = models.DateField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)


    def is_expired(self):
        return self.expiration_date and self.expiration_date < date.today()

    def is_expiring_soon(self, days=30):
        if not self.expiration_date:
            return False
        return date.today() <= self.expiration_date <= date.today() + timedelta(days=days)

    def __str__(self):
        return self.medicine.name

