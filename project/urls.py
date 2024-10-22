from django.urls import path, include
from app_api import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'tokens', views.TokenViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
