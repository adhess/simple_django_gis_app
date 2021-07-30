from django.urls import path
from rest_framework import routers
from .views import (ProviderViewSet, ServiceAreaViewSet, CoordinateViewSet, ServiceAreasByProviderViewSet,
                    CoordinatesByServiceArea)

router = routers.DefaultRouter()
router.register(r'api/provider', ProviderViewSet, 'provider')
router.register(r'api/service_area', ServiceAreaViewSet, 'service_area')
router.register(r'api/coordinate', CoordinateViewSet, 'coordinate')

urlpatterns = [
    path('api/service_areas_by_provider_id/', ServiceAreasByProviderViewSet.as_view()),
    path('api/coordinates_by_service_area/', CoordinatesByServiceArea.as_view()),
]

urlpatterns += router.urls

