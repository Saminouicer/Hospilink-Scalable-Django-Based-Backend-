# models.py
from django.db import models
from django.contrib.auth import get_user_model
# from inventory_management.models import Medicine

User = get_user_model()

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    organization = models.CharField(max_length=100, blank=True, null=True)
    managed_by = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='supplier_profile')

    def __str__(self):
        return self.name



class SupplierMedicine(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    medicine = models.ForeignKey('inventory_management.Medicine', on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('supplier', 'medicine')

    def __str__(self):
        return f"{self.supplier.name} - {self.medicine.name} (Stock: {self.stock_quantity})"



class MedicineRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('fulfilled', 'Fulfilled'),
    ]

    medicine = models.ForeignKey('inventory_management.Medicine', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity_requested = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    requested_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity_requested} x {self.medicine.name} from {self.supplier.name}"
