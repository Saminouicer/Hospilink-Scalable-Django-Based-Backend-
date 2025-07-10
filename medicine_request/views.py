# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Supplier, SupplierMedicine, MedicineRequest
from inventory_management.models import Medicine
from .serializers import SupplierSerializer, SupplierMedicineSerializer, MedicineRequestSerializer
from inventory_management.serializers import MedicineSerializer
from rest_framework.decorators import action

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(managed_by=self.request.user)

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated]


class SupplierMedicineViewSet(viewsets.ModelViewSet):
    queryset = SupplierMedicine.objects.all()
    serializer_class = SupplierMedicineSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            # Get supplier object linked to the current user
            supplier_qs = Supplier.objects.filter(managed_by=request.user)
            if not supplier_qs.exists():
                return Response({'detail': 'You are not assigned as a supplier.'}, status=400)

            supplier = supplier_qs.first()

            # Get medicine ID and quantity
            medicine_id = request.data.get('medicine')
            print(medicine_id)
            quantity = int(request.data.get('stock_quantity', 0))

            # Make sure the medicine exists
            try:
                medicine = Medicine.objects.get(id=medicine_id)
            except Medicine.DoesNotExist:
                return Response({'detail': 'Medicine not found.'}, status=404)

            # Create or update the SupplierMedicine record
            obj, created = SupplierMedicine.objects.get_or_create(
                supplier=supplier,
                medicine=medicine,
                defaults={'stock_quantity': quantity}
            )

            if not created:
                obj.stock_quantity += quantity
                obj.save()

            serializer = self.get_serializer(obj)
            return Response(serializer.data, status=201)

        except Exception as e:
            return Response({'detail': str(e)}, status=500)
        
    @action(detail=False, methods=['get'], url_path='medicine/(?P<medicine_id>[^/.]+)/suppliers')
    def get_suppliers_by_medicine(self, request, medicine_id=None):
        try:
            medicine = Medicine.objects.get(id=medicine_id)
            suppliers = medicine.suppliers.all()
            serializer = SupplierSerializer(suppliers, many=True)
            return Response(serializer.data)
        except Medicine.DoesNotExist:
            return Response({'detail': 'Medicine not found'}, status=404)



class MedicineRequestViewSet(viewsets.ModelViewSet):
    queryset = MedicineRequest.objects.all()
    serializer_class = MedicineRequestSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        supplier_id = data.get('supplier')
        medicine_id = data.get('medicine')
        quantity = int(data.get('quantity_requested', 0))

        try:
            supplier_med = SupplierMedicine.objects.get(supplier_id=supplier_id, medicine_id=medicine_id)
        except SupplierMedicine.DoesNotExist:
            return Response({"error": "This supplier does not provide the selected medicine."}, status=status.HTTP_400_BAD_REQUEST)

        if supplier_med.stock_quantity < quantity:
            return Response({"error": "Not enough stock available from this supplier."}, status=status.HTTP_400_BAD_REQUEST)

        supplier_med.stock_quantity -= quantity
        supplier_med.save()

        data['requested_by'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
