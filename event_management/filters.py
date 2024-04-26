import django_filters
from django_filters import DateFilter
from .models import *

class EventFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="start_date", lookup_expr='gte')
    class Meta:
        model = Event
        fields = ['title', 'location', 'type', 'tag']