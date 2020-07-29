from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pollsapi.tenant.views import ClientViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'client', ClientViewSet, base_name='clients')

urlpatterns = [
    path('', include(router.urls)),
]