from rest_framework.routers import SimpleRouter
from .viewsets import InvoiceViewSet

router = SimpleRouter()
router.register('invoices', InvoiceViewSet, base_name='invoices')
