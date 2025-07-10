from rest_framework.routers import DefaultRouter
from .views import SupplierMedicineViewSet, SupplierViewSet, MedicineRequestViewSet


router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'supplier-medicines', SupplierMedicineViewSet, basename='supplier-medicines')
router.register(r'medicine-requests', MedicineRequestViewSet)

urlpatterns = router.urls