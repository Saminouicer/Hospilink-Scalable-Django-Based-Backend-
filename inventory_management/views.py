from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Medicine, Batch
from .serializers import MedicineSerializer, BatchSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class MedicineViewSet(ModelViewSet):
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated]

    queryset = Medicine.objects.all().order_by('-created_at')


class BatchViewSet(ModelViewSet):
    serializer_class = BatchSerializer
    permission_classes = [IsAuthenticated]

    queryset = Batch.objects.all().order_by('-received_date')