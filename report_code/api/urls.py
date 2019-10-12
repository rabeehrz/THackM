from django.urls import path
from report_code.api.views import (
    
    api_detail_report_code_view,
    api_update_report_code_view,
    api_delete_report_code_view,
    api_create_report_code_view,

    )

app_name = 'report_code'

urlpatterns =[
    path('<id>', api_detail_report_code_view, name='detail'),
    path('<id>/update', api_update_report_code_view, name='update'),
    path('<id>/delete', api_delete_report_code_view, name='delete'),
    path('', api_create_report_code_view, name='create'),
]