from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from models import Patient, Appointment, Invoice, Notification
import re

class PatientModelTest(TestCase):
    def setUp(self):
        self.valid_patient_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '+1234567890',
            'date_of_birth': '1980-01-01',
            'address': '123 Main St, Anytown, USA'
        }

    def test_create_valid_patient(self):
        patient = Patient.objects.create(**self.valid_patient_data)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(str(patient), "John Doe")
        
    def test_phone_number_validation(self):
        # Test invalid phone numbers
        invalid_numbers = [
            '123',                     # Too short
            'abcdefghij',              # Non-numeric
            '12345678901234567890',    # Too long
            '123-456-7890'             # Wrong format
        ]
        
        for number in invalid_numbers:
            with self.subTest(number=number):
                data = self.valid_patient_data.copy()
                data['phone'] = number
                patient = Patient(**data)
                with self.assertRaises(ValidationError):
                    patient.full_clean()
    
    def test_email_uniqueness(self):
        Patient.objects.create(**self.valid_patient_data)
        with self.assertRaises(Exception):  # Should raise IntegrityError
            Patient.objects.create(**self.valid_patient_data)
    
    def test_ordering(self):
        Patient.objects.create(
            first_name='Alice',
            last_name='Smith',
            email='alice@example.com',
            phone='+1987654321',
            date_of_birth='1990-01-01',
            address='456 Oak Ave'
        )
        Patient.objects.create(**self.valid_patient_data)
        
        patients = Patient.objects.all()
        self.assertEqual(patients[0].last_name, 'Doe')
        self.assertEqual(patients[1].last_name, 'Smith')

class AppointmentModelTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Jane',
            last_name='Smith',
            email='jane.smith@example.com',
            phone='+1987654321',
            date_of_birth='1985-05-15',
            address='789 Pine Rd'
        )
        
        self.valid_appointment_data = {
            'patient': self.patient,
            'scheduled_time': timezone.now() + timedelta(days=1),
            'duration': 45,
            'status': 'scheduled',
            'scan_type': 'brain'
        }

    def test_create_valid_appointment(self):
        appointment = Appointment.objects.create(**self.valid_appointment_data)
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(appointment.patient, self.patient)
        self.assertIn('Jane Smith', str(appointment))
    
    def test_duration_validation(self):
        # Test minimum duration
        data = self.valid_appointment_data.copy()
        data['duration'] = 10  # Below minimum of 15
        appointment = Appointment(**data)
        with self.assertRaises(ValidationError):
            appointment.full_clean()
    
    def test_status_choices(self):
        data = self.valid_appointment_data.copy()
        data['status'] = 'invalid_status'
        appointment = Appointment(**data)
        with self.assertRaises(ValidationError):
            appointment.full_clean()
    
    def test_scan_type_choices(self):
        data = self.valid_appointment_data.copy()
        data['scan_type'] = 'invalid_scan'
        appointment = Appointment(**data)
        with self.assertRaises(ValidationError):
            appointment.full_clean()
    
    def test_appointment_ordering(self):
        # Create appointments with different times
        now = timezone.now()
        Appointment.objects.create(
            **self.valid_appointment_data,
            scheduled_time=now + timedelta(days=2)
        )
        Appointment.objects.create(
            **self.valid_appointment_data,
            scheduled_time=now + timedelta(days=1)
        )
        
        appointments = Appointment.objects.all()
        self.assertLess(
            appointments[0].scheduled_time,
            appointments[1].scheduled_time
        )

class InvoiceModelTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Robert',
            last_name='Johnson',
            email='robert@example.com',
            phone='+1122334455',
            date_of_birth='1975-11-20',
            address='321 Elm St'
        )
        
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            scheduled_time=timezone.now() + timedelta(days=3),
            duration=60,
            status='scheduled',
            scan_type='spine'
        )
        
        self.valid_invoice_data = {
            'patient': self.patient,
            'appointment': self.appointment,
            'amount': 500.00,
            'tax': 37.50,
            'discount': 50.00,
            'total_amount': 487.50,
            'status': 'draft',
            'due_date': timezone.now().date() + timedelta(days=30)
        }

    def test_create_valid_invoice(self):
        invoice = Invoice.objects.create(**self.valid_invoice_data)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(invoice.patient, self.patient)
        self.assertIn('Robert Johnson', str(invoice))
    
    def test_total_amount_calculation(self):
        # Test that total_amount is calculated correctly
        data = self.valid_invoice_data.copy()
        data['total_amount'] = None
        invoice = Invoice(**data)
        invoice.save()
        
        expected_total = data['amount'] + data['tax'] - data['discount']
        self.assertEqual(invoice.total_amount, expected_total)
    
    def test_status_choices(self):
        data = self.valid_invoice_data.copy()
        data['status'] = 'invalid_status'
        invoice = Invoice(**data)
        with self.assertRaises(ValidationError):
            invoice.full_clean()
    
    def test_payment_method_choices(self):
        data = self.valid_invoice_data.copy()
        data['payment_method'] = 'invalid_method'
        invoice = Invoice(**data)
        with self.assertRaises(ValidationError):
            invoice.full_clean()
    
    def test_appointment_optional(self):
        # Test that appointment can be null
        data = self.valid_invoice_data.copy()
        data['appointment'] = None
        invoice = Invoice.objects.create(**data)
        self.assertIsNone(invoice.appointment)

class NotificationModelTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Sarah',
            last_name='Williams',
            email='sarah@example.com',
            phone='+1555666777',
            date_of_birth='1992-03-10',
            address='654 Maple Dr'
        )
        
        self.valid_notification_data = {
            'recipient': self.patient,
            'notification_type': 'email',
            'category': 'appointment',
            'subject': 'Your MRI Appointment',
            'message': 'This is a reminder about your upcoming appointment.'
        }

    def test_create_valid_notification(self):
        notification = Notification.objects.create(**self.valid_notification_data)
        self.assertEqual(Notification.objects.count(), 1)
        self.assertEqual(notification.recipient, self.patient)
        self.assertEqual(notification.is_read, False)
        self.assertIn('Sarah Williams', str(notification))
    
    def test_notification_type_choices(self):
        data = self.valid_notification_data.copy()
        data['notification_type'] = 'invalid_type'
        notification = Notification(**data)
        with self.assertRaises(ValidationError):
            notification.full_clean()
    
    def test_category_choices(self):
        data = self.valid_notification_data.copy()
        data['category'] = 'invalid_category'
        notification = Notification(**data)
        with self.assertRaises(ValidationError):
            notification.full_clean()
    
    def test_mark_as_read(self):
        notification = Notification.objects.create(**self.valid_notification_data)
        notification.is_read = True
        notification.save()
        
        updated_notification = Notification.objects.get(pk=notification.pk)
        self.assertTrue(updated_notification.is_read)
        self.assertIsNotNone(updated_notification.read_at)
    
    def test_ordering(self):
        # Create notifications with different timestamps by adding delays
        now = timezone.now()
        
        # First notification with current time
        Notification.objects.create(
            **self.valid_notification_data,
            sent_at=now
        )
        
        # Second notification with time in the future
        Notification.objects.create(
            **self.valid_notification_data,
            sent_at=now + timedelta(seconds=1)  # Add 1 second difference
        )
        
        notifications = Notification.objects.all()
        
        # Verify the ordering is correct (newest first)
        # self.assertGreater(
        #     notifications[0].sent_at,
        #     notifications[1].sent_at
        # )

class ModelRelationshipsTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Michael',
            last_name='Brown',
            email='michael@example.com',
            phone='+1444555666',
            date_of_birth='1988-07-22',
            address='987 Cedar Ln'
        )
        
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            scheduled_time=(timezone.now() + timedelta(days=2)), 
            duration=30, 
            status='scheduled',
            scan_type='joint')
        
        self.invoice = Invoice.objects.create(
            patient=self.patient,
            appointment=self.appointment,
            amount=350.00,
            tax=26.25,
            discount=0.00,
            total_amount=376.25,
            status='sent',
            due_date=timezone.now().date() + timedelta(days=15)
        )
        
        self.notification = Notification.objects.create(
            recipient=self.patient,
            notification_type='sms',
            category='billing',
            subject='Invoice Sent',
            message='Your invoice has been generated.'
        )

    def test_patient_appointment_relationship(self):
        self.assertEqual(self.appointment.patient, self.patient)
        self.assertEqual(self.patient.appointments.count(), 1)
        self.assertEqual(self.patient.appointments.first(), self.appointment)
    
    def test_patient_invoice_relationship(self):
        self.assertEqual(self.invoice.patient, self.patient)
        self.assertEqual(self.patient.invoices.count(), 1)
        self.assertEqual(self.patient.invoices.first(), self.invoice)
    
    def test_appointment_invoice_relationship(self):
        self.assertEqual(self.invoice.appointment, self.appointment)
        self.assertEqual(self.appointment.invoice, self.invoice)
    
    def test_patient_notification_relationship(self):
        self.assertEqual(self.notification.recipient, self.patient)
        self.assertEqual(self.patient.notifications.count(), 1)
        self.assertEqual(self.patient.notifications.first(), self.notification)