from images.api.views import ImageViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]