from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet ,BatchViewSet


router = DefaultRouter()
router.register(r'medicines', MedicineViewSet, basename='medicines')
router.register(r'batches', BatchViewSet, basename='batches')

urlpatterns = router.urls