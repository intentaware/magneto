from rest_framework.routers import SimpleRouter
from .viewsets import CompanyViewSet, CircleViewSet

router = SimpleRouter()
router.register('companies', CompanyViewSet, base_name='campanies')
router.register('circles', CircleViewSet)
