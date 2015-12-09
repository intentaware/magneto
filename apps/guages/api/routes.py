from rest_framework.routers import SimpleRouter

from .viewsets import AssetViewSet

router = SimpleRouter()
router.register('assets', AssetViewSet, base_name='assets')
