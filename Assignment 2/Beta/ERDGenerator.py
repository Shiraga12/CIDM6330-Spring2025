from graphviz import Digraph

# Create an enhanced ERD diagram
erd = Digraph('ERD', filename='enhanced_mri_care_manager_erd', format='png')

# Define entities
erd.node('Patient', 'Patient\n- id (PK)\n- name\n- email\n- phone')
erd.node('Doctor', 'Doctor\n- id (PK)\n- name\n- specialty\n- phone')
erd.node('Appointment', 'Appointment\n- id (PK)\n- patient_id (FK)\n- doctor_id (FK)\n- date\n- status (ENUM)')
erd.node('Invoice', 'Invoice\n- id (PK)\n- patient_id (FK)\n- appointment_id (FK)\n- amount\n- status (ENUM)')
erd.node('Notification', 'Notification\n- id (PK)\n- patient_id (FK)\n- type\n- message\n- sent_at')

# Define relationships
erd.edge('Patient', 'Appointment', label='1 to Many')
erd.edge('Doctor', 'Appointment', label='1 to Many')
erd.edge('Patient', 'Invoice', label='1 to Many')
erd.edge('Appointment', 'Invoice', label='1 to 1')
erd.edge('Patient', 'Notification', label='1 to Many')

# Render and save the diagram
erd_path = "/mnt/data/enhanced_mri_care_manager_erd.png"
erd.render(filename="enhanced_mri_care_manager_erd", format='png', cleanup=True)

# Return the generated ERD diagram path
# erd_path