from django.urls import path
from cases.api.views import (
    
    api_detail_cases_view,
    api_update_cases_view,
    api_delete_cases_view,
    api_create_cases_view,

    )

app_name = 'cases'

urlpatterns =[
    path('<id>', api_detail_cases_view, name='detail'),
    path('<id>/update', api_update_cases_view, name='update'),
    path('<id>/delete', api_delete_cases_view, name='delete'),
    path('', api_create_cases_view, name='create'),
]