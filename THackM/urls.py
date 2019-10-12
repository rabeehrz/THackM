from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/users/', include('users.api.urls', 'users_api')),
    path('admin/', admin.site.urls),
]
