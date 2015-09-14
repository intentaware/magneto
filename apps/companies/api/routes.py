from rest_framework.routers import SimpleRouter
from .viewsets import CompanyViewSet

router = SimpleRouter()
router.register('companies', CompanyViewSet, base_name='campanies')
