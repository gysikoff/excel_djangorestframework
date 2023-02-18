from django.urls import path, include
from rest_framework import routers
from .views import UploadExcelViewSet

router = routers.DefaultRouter()
router.register('', UploadExcelViewSet, basename="upload-excel")

urlpatterns = [
    path('', include(router.urls)),
]