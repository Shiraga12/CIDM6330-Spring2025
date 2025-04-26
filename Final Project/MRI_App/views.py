from rest_framework import viewsets
from .models import Patient, Appointment, Invoice, Notification
from .serializers import PatientSerializer, AppointmentSerializer, InvoiceSerializer, NotificationSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')