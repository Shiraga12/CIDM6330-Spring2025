from django.db import models
from django.core.validators import MinValueValidator, RegexValidator

class Patient(models.Model):
    """
    Represents a patient in the MRI care system
    """
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'"
    )
    phone = models.CharField(validators=[phone_regex], max_length=17)
    date_of_birth = models.DateField()
    address = models.TextField()
    insurance_provider = models.CharField(max_length=100, blank=True, null=True)
    insurance_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name_plural = "Patients"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    """
    Represents an MRI appointment
    """
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
        ('no_show', 'No Show'),
    ]
    
    SCAN_TYPE_CHOICES = [
        ('brain', 'Brain MRI'),
        ('spine', 'Spine MRI'),
        ('joint', 'Joint MRI'),
        ('abdominal', 'Abdominal MRI'),
        ('cardiac', 'Cardiac MRI'),
    ]

    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    scheduled_time = models.DateTimeField()
    duration = models.PositiveIntegerField(
        default=30,
        validators=[MinValueValidator(15)],
        help_text="Duration in minutes"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled'
    )
    scan_type = models.CharField(
        max_length=20,
        choices=SCAN_TYPE_CHOICES
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['scheduled_time']
        indexes = [
            models.Index(fields=['scheduled_time']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f"{self.patient} - {self.scheduled_time}"


class Invoice(models.Model):
    """
    Represents a billing invoice for services
    """
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('insurance', 'Insurance'),
        ('credit', 'Credit Card'),
        ('check', 'Check'),
        ('cash', 'Cash'),
    ]

    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='invoices'
    )
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        blank=True,
        null=True
    )
    due_date = models.DateField()
    paid_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Invoices"

    def __str__(self):
        return f"Invoice #{self.id} - {self.patient}"


class Notification(models.Model):
    """
    Represents system notifications sent to patients or staff
    """
    NOTIFICATION_TYPES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('push', 'Push Notification'),
    ]

    NOTIFICATION_CATEGORIES = [
        ('appointment', 'Appointment'),
        ('billing', 'Billing'),
        ('system', 'System'),
    ]

    id = models.BigAutoField(primary_key=True)
    recipient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES
    )
    category = models.CharField(
        max_length=20,
        choices=NOTIFICATION_CATEGORIES
    )
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-sent_at']
        indexes = [
            models.Index(fields=['recipient']),
            models.Index(fields=['is_read']),
        ]

    def __str__(self):
        return f"{self.get_notification_type_display()} to {self.recipient}"