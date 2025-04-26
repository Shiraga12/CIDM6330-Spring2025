from django.test import TestCase
from MRI_App.models import Patient, Appointment, Invoice

class InvoiceModelTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="Alice",
            last_name="Brown",
            date_of_birth="1970-12-12",
            email="alice.brown@example.com",
            phone_number="5551234567"
        )
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            appointment_date="2025-06-01T09:00:00Z",
            description="Spinal MRI"
        )

    def test_create_invoice(self):
        invoice = Invoice.objects.create(
            appointment=self.appointment,
            amount=500.00,
            paid=False
        )
        self.assertEqual(str(invoice), f"Invoice {invoice.id} for {self.appointment}")
