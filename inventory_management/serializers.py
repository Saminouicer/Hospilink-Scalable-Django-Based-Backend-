from rest_framework import serializers
from .models import Batch, Medicine

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'id', 'name', 'description', 'category', 'created_at',
            'low_stock_threshold',
            'total_quantity',
            'is_low_stock',
        ]
        read_only_fields = ['id', 'created_at', 'total_quantity', 'is_low_stock']

    def get_total_quantity(self, obj):
        return obj.total_quantity()

    def get_is_low_stock(self, obj):
        return obj.is_low_stock()
    

    

class BatchSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='medicine.name', read_only=True)

    class Meta:
        model = Batch
        fields = [
            'id',
            'medicine',
            'medicine_name',
            'quantity',
            'expiration_date',
            'received_date',
            'is_delivered',
        ]
        read_only_fields = ['id', 'received_date', 'medicine_name']