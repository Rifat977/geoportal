from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Country
from .serializers import CountrySerializer
from rest_framework import status


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_common', 'name_official']

    @action(detail=True, methods=['get'])
    def same_region(self, request, pk=None):
        country = self.get_object()
        regional_countries = Country.objects.filter(region=country.region).exclude(pk=country.pk)
        serializer = self.get_serializer(regional_countries, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='language/(?P<lang_code>[a-z]{3})')
    def by_language(self, request, lang_code=None):
        countries = Country.objects.filter(languages__has_key=lang_code)
        serializer = self.get_serializer(countries, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request):
        query = request.query_params.get('search', '')
        if not query:
            return Response({'detail': "Query param is required."}, status=400)
        results = self.queryset.filter(name_common__icontains=query)
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data)
