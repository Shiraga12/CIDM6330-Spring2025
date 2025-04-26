from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    scheduled_date = models.DateTimeField()
    mri_type = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"MRI for {self.patient} on {self.scheduled_date}"

class Invoice(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='invoice')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    issued_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Invoice #{self.id} - {self.amount}"

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES)

    def __str__(self):
        return f"Notification for {self.appointment} ({self.notification_type})"
