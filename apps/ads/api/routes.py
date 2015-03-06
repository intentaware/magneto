from rest_framework.routers import SimpleRouter

from .viewsets import AdViewSet

router = SimpleRouter()

router.register('ads', AdViewSet)
