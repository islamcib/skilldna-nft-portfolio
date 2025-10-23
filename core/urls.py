from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkillNFTViewSet

router = DefaultRouter()
router.register(r'skills', SkillNFTViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
