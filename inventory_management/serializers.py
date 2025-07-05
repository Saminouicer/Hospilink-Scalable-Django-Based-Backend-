from datetime import date, timedelta
from rest_framework import serializers
from .models import Batch, Medicine




class BatchSerializer(serializers.ModelSerializer):

    medicine_name = serializers.CharField(source='medicine.name', read_only=True)
    is_expired = serializers.SerializerMethodField()
    is_expiring_soon = serializers.SerializerMethodField()

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
            'is_expired',         
            'is_expiring_soon',
            'updated_at',
        ]
        read_only_fields = ['id', 'received_date', 'medicine_name', 'is_expired', 'is_expiring_soon','updated_at']

    def get_is_expired(self, obj):
        return obj.is_expired()

    def get_is_expiring_soon(self, obj):
        return obj.is_expiring_soon()
    




class MedicineSerializer(serializers.ModelSerializer):

    total_quantity = serializers.SerializerMethodField()
    is_low_stock = serializers.SerializerMethodField()
    batches = BatchSerializer(many=True, read_only=True)


    class Meta:
        model = Medicine
        fields = [
            'id', 'name', 'description', 'category', 'created_at','batches',
            'low_stock_threshold',
            'total_quantity',
            'is_low_stock',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'total_quantity', 'is_low_stock','updated_at']

    def get_total_quantity(self, obj):
        return obj.total_quantity()

    def get_is_low_stock(self, obj):
        return obj.is_low_stock()
    
