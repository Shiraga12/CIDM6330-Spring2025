from graphviz import Digraph

# Create an ERD diagram
erd = Digraph('ERD', filename='mri_care_manager_erd', format='png')

# Define entities
erd.node('Patient', 'Patient\n- id (PK)\n- name\n- email\n- phone')
erd.node('Appointment', 'Appointment\n- id (PK)\n- patient_id (FK)\n- date\n- status')
erd.node('Invoice', 'Invoice\n- id (PK)\n- patient_id (FK)\n- amount\n- status')
erd.node('Notification', 'Notification\n- id (PK)\n- patient_id (FK)\n- type\n- message\n- sent_at')

# Define relationships
erd.edge('Patient', 'Appointment', label='1 to Many')
erd.edge('Patient', 'Invoice', label='1 to Many')
erd.edge('Patient', 'Notification', label='1 to Many')

# Render and save the diagram
erd_path = "/mnt/data/mri_care_manager_erd.png"
erd.render(filename=erd_path, format='png', cleanup=False)

# Return the generated ERD diagram path
erd_path

