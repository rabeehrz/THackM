from django.urls import path
from reports.api.views import (
    
    api_detail_reports_view,
    api_update_reports_view,
    api_delete_reports_view,
    api_create_reports_view,
    api_accept_reports_view,
    api_decline_reports_view,

    )

app_name = 'reports'

urlpatterns =[
    path('<id>', api_detail_reports_view, name='detail'),
    path('<id>/accept', api_accept_reports_view, name='accept'),
    path('<id>/decline', api_decline_reports_view, name='decline'),
    path('<id>/update', api_update_reports_view, name='update'),
    path('<id>/delete', api_delete_reports_view, name='delete'),
    path('', api_create_reports_view, name='create'),
]