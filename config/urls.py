from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/attendance/", include("apps.attendance.urls")),
    path("api/employees/", include("apps.employees.urls")),
]
