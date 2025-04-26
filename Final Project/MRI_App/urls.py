from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, AppointmentViewSet, InvoiceViewSet, NotificationViewSet, home

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', home, name='home'),  # This will route to the home page
]