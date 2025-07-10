# serializers.py
from rest_framework import serializers
from .models import Supplier, SupplierMedicine, MedicineRequest
from django.contrib.auth import get_user_model

User = get_user_model()

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierMedicine
        fields = '__all__'

class MedicineRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineRequest
        fields = '__all__'