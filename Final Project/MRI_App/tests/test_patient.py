from django.test import TestCase
from MRI_App.models import Patient

class PatientModelTest(TestCase):

    def test_create_patient(self):
        patient = Patient.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth="1990-01-01",
            email="john.doe@example.com",
            phone_number="1234567890"
        )
        self.assertEqual(str(patient), "John Doe")
        self.assertEqual(patient.email, "john.doe@example.com")
