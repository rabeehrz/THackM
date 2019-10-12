from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/users/', include('users.api.urls', 'users_api')),
    path('api/cases/', include('cases.api.urls', 'cases_api')),
    path('api/reports/', include('reports.api.urls', 'reports_api')),
    path('api/report_code/', include('report_code.api.urls', 'report_code_api')),
    path('admin/', admin.site.urls),
]
