from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from apps.finances.models import Invoice

from .serializers import InvoiceSerializer, InvoiceChargeSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.filter(
            company_id=self.request.session['company'])

    @detail_route(methods=['post'], url_path='charge')
    def charge(self, request, pk):
        invoice = Invoice.objects.get(id=pk)
        srlzr = InvoiceChargeSerializer(data=request.data)
        srlzr.invoice = invoice
        if srlzr.is_valid():
            return Response(status=200)
        else:
            return Response(srlzr.errors, status=400)
