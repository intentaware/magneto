from rest_framework.routers import SimpleRouter

from .viewsets import CampaignViewSet

router = SimpleRouter()
router.register('campaigns', CampaignViewSet, base_name='campaigns')
