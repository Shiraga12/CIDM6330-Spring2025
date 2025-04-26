from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MRI_App.urls')),  # Include MRI_App's URL patterns
]
