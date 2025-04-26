# Feature 1: Create Patient
Feature: Patient Registration

  Scenario: Admin successfully creates a patient record
    Given an admin is logged into the system
    When the admin submits a new patient form with valid details
    Then a new patient should be added to the database
# Feature 2: Schedule Appointment
Feature: Appointment Scheduling

  Scenario: Patient schedules an MRI appointment
    Given a registered patient exists
    When the patient selects a date and time for the MRI
    Then an appointment should be created and linked to the patient

# Feature 3: Create Invoice after MRI Scan
Feature: Invoice Generation

  Scenario: Admin generates invoice after MRI scan
    Given a completed MRI scan exists
    When the admin generates an invoice for the scan
    Then the invoice should be saved with the correct patient and amount
