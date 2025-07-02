from django.contrib import admin
from .models import Batch, Medicine

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category','created_at')
    search_fields = ('name', 'category')
    list_filter = ('category',)



class BatchAdmin(admin.ModelAdmin):
    list_display = ('id','quantity','expiration_date','received_date', 'is_delivered')
    search_fields = ('medicine__name', 'expiration_date', 'received_date', 'is_delivered')
    list_filter = ('expiration_date','received_date','is_delivered')


admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Batch, BatchAdmin)
