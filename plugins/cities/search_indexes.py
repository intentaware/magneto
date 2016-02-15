from haystack import indexes
from plugins.cities.models import City

class CityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return City

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
