from rest_framework.routers import SimpleRouter
from .viewsets import CircleViewSet, CampaignCircleViewSet

router = SimpleRouter()
router.register('circles', CircleViewSet, base_name='circles')
router.register('campaign-circles', CampaignCircleViewSet, base_name='campaign_circles')
