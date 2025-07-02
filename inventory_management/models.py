from django.db import models
# Create your models here.

class Medicine(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    category=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Batch(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='batches')
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField()
    received_date = models.DateField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.medicine.name

