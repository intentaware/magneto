from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
