# MRI Care Manager - Requirements Specification

(C) 2025 Toluwani Adeoti. All Rights Reserved.

## **Table of Contents**
1. [Introduction](#introduction)
2. [Requirements Statements](#requirements-statements)
3. [User Stories, Use Cases, Features, Gherkin Validation](#user-stories-use-cases-features-gherkin-validation)
4. [Specifications](#specifications)
   - [Concept](#concept)
   - [UX Notes](#ux-notes)
   - [Interfaces (Controls)](#interfaces-controls)
   - [Behaviors](#behaviors)
   - [Feature/Package A - Appointment Scheduling System](#featurepackage-a)
   - [Feature/Package N - Notification System](#featurepackage-n)
5. [UML Diagrams](#uml-diagrams)

---

## **Introduction**
### **Problem Description**
Managing patient collections and appointment scheduling is a persistent challenge for small healthcare businesses, such as independent MRI centers. These businesses often rely on outdated systems or manual processes, leading to inefficiencies, missed payments, and scheduling conflicts.

### **Domain of Practice**
The domain for this problem is healthcare administration, focusing on small diagnostic imaging centers like MRI facilities. The software aims to optimize administrative tasks such as patient billing, appointment scheduling, and payment tracking.

### **Project Motivation**
I have a personal interest in this domain because my father has managed an MRI center since 2019. I have witnessed firsthand the administrative challenges he faced in managing patient collections. As a software developer, I want to create solutions that help small businesses streamline operations and focus on growth.

---

## **Requirements Statements**
### **Functional Requirements**
1. The system shall allow patients to schedule, reschedule, and cancel appointments online.
2. The system shall send appointment reminders via email and SMS.
3. The system shall generate automated invoices for patient billing.
4. The system shall track payments and notify staff of overdue balances.
5. The system shall provide analytics dashboards for revenue tracking and patient visit trends.

### **Non-Functional Requirements**
1. The system shall ensure data security through HIPAA-compliant encryption.
2. The system shall maintain an uptime of 99.9%.
3. The system shall support scalability for multiple MRI centers.

---

## **User Stories, Use Cases, Features, Gherkin Validation**

### **User Stories**
1. **As a patient**, I want to schedule an MRI appointment online so that I can avoid calling the office.
2. **As an administrator**, I want to generate invoices automatically so that I can streamline patient billing.
3. **As a manager**, I want to view a report on monthly revenue so that I can analyze business performance.

### **Use Case: Appointment Scheduling**
**Actors:** Patient, Administrator  
**Precondition:** Patient must have an account  
**Steps:**
1. Patient selects an available time slot.
2. Patient confirms the appointment.
3. System sends a confirmation email/SMS.

### **Gherkin Validation (Example for Appointment Reminders)**
```gherkin
Feature: Appointment Reminder System
  Scenario: Sending an appointment reminder to a patient
    Given a patient has a scheduled appointment
    When the appointment date is approaching
    Then the system should send an email and SMS reminder
```

## **Specifications**
### **Concept**
The **MRI Care Manager** is designed to streamline the workflow of small MRI centers by automating appointment scheduling, billing, and payment tracking. It provides an intuitive interface for patients and administrators to manage bookings and payments efficiently.

### **UX Notes**
- **Simple and Clear Navigation:** The user interface should be straightforward, allowing patients to book and manage appointments easily.
- **Mobile Compatibility:** The system should be accessible on desktops, tablets, and smartphones.
- **Automated Notifications:** Patients should receive clear and timely appointment reminders and payment alerts.

### **Interfaces (Controls)**
The system will feature several interfaces to accommodate different user interactions:

#### **1. Patient Portal**
- **Controls:**
  - `Schedule Appointment` (Button) → Opens the appointment booking form.
  - `View Appointments` (List) → Displays all upcoming and past appointments.
  - `Cancel/Reschedule` (Button) → Allows modifying or canceling an appointment.
  - `Make Payment` (Button) → Redirects to the payment processing page.
  - `Download Invoice` (Button) → Provides a PDF of the billing statement.

#### **2. Administrator Dashboard**
- **Controls:**
  - `Manage Appointments` (Table/List) → Displays all patient bookings.
  - `Send Notification` (Button) → Manually trigger appointment reminders.
  - `Generate Reports` (Dropdown) → Provides revenue and appointment analytics.
  - `Update Patient Information` (Form) → Allows editing patient records.
  - `Approve/Reject Refunds` (Button) → Handles patient refund requests.

#### **3. Notification System**
- **Controls:**
  - `Enable/Disable Notifications` (Toggle) → Allows users to turn notifications on or off.
  - `Select Notification Type` (Dropdown) → Options include Email, SMS, or Push Notification.
  - `Set Reminder Frequency` (Dropdown) → Choices: 24 hours before, 1 hour before, etc.

### **Behaviors**
The system consists of multiple functional behaviors that define how users interact with the system and how processes are automated.

#### **1. Appointment Scheduling Behavior**
- Patients select available time slots for MRI appointments.
- The system updates availability in real-time to prevent double-booking.
- Patients receive automated confirmation via email and SMS.
- Administrators can manually adjust bookings and override restrictions if necessary.

#### **2. Billing and Payment Behavior**
- The system automatically generates an invoice upon appointment confirmation.
- Patients can make payments via integrated payment gateways (Credit/Debit, PayPal, Insurance).
- Payment reminders are sent via email and SMS if an invoice remains unpaid.
- Administrators can track outstanding balances and overdue payments.

#### **3. Notification System Behavior**
- Automated reminders are sent to patients before their appointment.
- Notifications are sent to administrators when an appointment is canceled or rescheduled.
- Payment reminders are triggered for overdue invoices.

#### **4. Report Generation Behavior**
- The system aggregates appointment and payment data to generate monthly reports.
- Administrators can export reports in CSV/PDF format.
- The dashboard provides insights into patient flow, revenue trends, and system usage.

---

## **Feature/Package A**
### Appointment Scheduling System
The appointment scheduling system enables patients to book, reschedule, and cancel appointments seamlessly.

**Key Components:**
- **Appointment_Creation_Form Class**: Handles new appointment requests.
- **Availability_Checker Class**: Ensures that selected time slots are open.
- **Appointment_Notification Class**: Sends confirmation messages to patients.

**UML Diagram:**
![Appointment Scheduling UML](/Assignment%201/Appointment_Scheduling_UML.png)

---

## **Feature/Package N**
### Notification System
The notification system ensures timely updates for both patients and administrators.

**Key Components:**
- **Notification_Manager Class**: Handles different notification types (Email, SMS, Push).
- **Reminder_Scheduler Class**: Triggers automated reminders before appointments.
- **Admin_Alert Class**: Notifies administrators of cancellations, reschedules, or no-shows.

**UML Diagram:**
![Notification System UML](/Assignment%201/Notification_System_UML.png)

---
