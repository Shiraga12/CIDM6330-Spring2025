# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import Appointment, Notification, Invoice

@shared_task
def send_appointment_reminder(appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    subject = f"Reminder: MRI Appointment on {appointment.appointment_time}"
    message = f"Hello {appointment.patient.name},\n\nThis is a reminder..."
    
    # Send email
    send_mail(
        subject,
        message,
        'noreply@mricare.com',
        [appointment.patient.email],
        fail_silently=False,
    )
    
    # Record notification
    Notification.objects.create(
        patient=appointment.patient,
        notification_type='email',
        message=message
    )

@shared_task
def generate_invoice(appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    # Invoice generation logic
    invoice = Invoice.objects.create(
        appointment=appointment,
        amount=500.00,  # Example amount
        due_date=appointment.appointment_time.date()  # Due on appointment date
    )
    return invoice.id