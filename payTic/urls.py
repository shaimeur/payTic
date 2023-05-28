from django.contrib import admin
from django.urls import path
from ETLAPI import views # Import views.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('import_csv/', views.import_csv),
]
