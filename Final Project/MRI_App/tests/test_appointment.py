from django.test import TestCase
from MRI_App.models import Patient, Appointment

class AppointmentModelTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="Jane",
            last_name="Smith",
            date_of_birth="1985-06-15",
            email="jane.smith@example.com",
            phone_number="0987654321"
        )

    def test_create_appointment(self):
        appointment = Appointment.objects.create(
            patient=self.patient,
            appointment_date="2025-05-01T10:00:00Z",
            description="MRI Brain Scan"
        )
        self.assertEqual(str(appointment), "Jane Smith - 2025-05-01 10:00:00+00:00")
