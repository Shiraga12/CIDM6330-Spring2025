from django.test import TestCase
from MRI_App.models import Patient, Appointment, Notification

class NotificationModelTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="Bob",
            last_name="Taylor",
            date_of_birth="1980-07-22",
            email="bob.taylor@example.com",
            phone_number="1112223333"
        )
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            appointment_date="2025-07-10T14:00:00Z",
            description="Knee MRI"
        )

    def test_create_notification(self):
        notification = Notification.objects.create(
            appointment=self.appointment,
            message="Reminder: Your MRI appointment is scheduled tomorrow.",
            sent=False
        )
        self.assertEqual(str(notification), f"Notification for {self.appointment}")
