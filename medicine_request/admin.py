from django.contrib import admin
from .models import Supplier, MedicineRequest, SupplierMedicine

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'contact_email', 'managed_by')
    search_fields = ('name', 'organization', 'contact_email')
    list_filter = ('organization',)

@admin.register(MedicineRequest)
class MedicineRequestAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'supplier', 'quantity_requested', 'status', 'requested_by', 'created_at', 'updated_at')
    search_fields = ('medicine__name', 'supplier__name', 'requested_by__username')
    list_filter = ('status', 'supplier')

@admin.register(SupplierMedicine)
class SupplierMedicineAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'medicine', 'stock_quantity')
    search_fields = ('supplier__name', 'medicine__name')
    list_filter = ('supplier',)
