from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkillNFTViewSet
from .certificate_views import CertificateView

router = DefaultRouter()
router.register(r'skills', SkillNFTViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('certificate/<int:skill_id>/', CertificateView.as_view(), name='certificate'),
]
