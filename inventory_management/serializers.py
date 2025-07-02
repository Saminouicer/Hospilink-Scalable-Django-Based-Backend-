from rest_framework import serializers
from .models import Batch, Medicine

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model: Medicine
        fields = ['id', 'name', 'description', 'category','created_at']
        read_only_fields = ['id', 'created_at']



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