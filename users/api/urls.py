from django.urls import path
from users.api.views import (
    
    api_detail_users_view,
    api_update_users_view,
    api_delete_users_view,
    api_create_users_view,
 
    )

app_name = 'users'

urlpatterns =[
    
    path('<id>', api_detail_users_view, name='detail'),
    path('<id>/update', api_update_users_view, name='update'),
    path('<id>/delete', api_delete_users_view, name='delete'),
    path('', api_create_users_view, name='create'),
    
]