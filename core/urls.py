from django.urls import path
from .views import CountryViewSet
from . import views

country_list = CountryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

country_detail = CountryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

same_region = CountryViewSet.as_view({
    'get': 'same_region'
})

by_language = CountryViewSet.as_view({
    'get': 'by_language'
})

search = CountryViewSet.as_view({
    'get': 'search'
})

urlpatterns = [
    path('', country_list, name='country-list'),
    path('<int:pk>/', country_detail, name='country-detail'),
    path('<int:pk>/same-region/', same_region, name='country-same-region'),
    path('language/<str:lang_code>/', by_language, name='country-by-language'),
    path('search/', search, name='country-search'), 

    path('countries/', views.country_list_view, name='country-list-view'),
    path('countries/<int:pk>/', views.country_detail_view, name='country-detail-view'),
]
