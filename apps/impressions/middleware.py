from django.conf import settings


class ImpressionMiddleware(object):

    def process_request(self, request):
        publisher_key = request.META.get('HTTP_PUBLISHER_KEY', None)
        if publisher_key:
            from apps.companies.models import Company
            try:
                company = Company.objects.get(publisher_key=publisher_key)
                request.company = company
            except Company.DoesNotExist:
                request.company = None

    def process_response(self, request, response):
        company = getattr(request, 'company', None)
        if company:
            print company
        return response
