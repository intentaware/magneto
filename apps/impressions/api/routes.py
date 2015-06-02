from rest_framework.routers import SimpleRouter
from .views import ImpressionViewSet

router = SimpleRouter()

router.register('impressions', ImpressionViewSet, base_name="impressions")
