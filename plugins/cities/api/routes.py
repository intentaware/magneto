from rest_framework.routers import SimpleRouter
from .viewsets import CityViewSet

router = SimpleRouter()
router.register('cities', CityViewSet, base_name='cites')
