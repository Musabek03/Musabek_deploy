from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,CategoryViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'products',ProductViewSet)
router.register(r'category',CategoryViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls))
]