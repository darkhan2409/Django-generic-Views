from django.urls import path
from .views import *

urlpatterns = [
    path('countries', CountryList.as_view(), name='country_list_url'),
    path('country/<int:pk>', CountryDetail.as_view(), name='country_detail_url'),
    path('country/create', CountryCreate.as_view(), name='country_create_url'),
    path('country/update/<int:pk>', CountryUpdate.as_view(), name='country_update_url'),
    path('country/delete/<int:pk>', CountryDelete.as_view(), name='country_delete_url'),
]
