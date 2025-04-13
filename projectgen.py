import os

# Define the base path
base_path = r"C:\Users\HP\GitHub\CIDM6330-Spring2025\Assignment 5"

# Define the folder structure
folders = [
    "myproject",
    "myapi",
    "myapi/tests",
]

# Define the files to create
files = [
    "myproject/manage.py",
    "myapi/models.py",
    "myapi/views.py",
    "myapi/serializers.py",
    "myapi/tasks.py",
    "myapi/tests/__init__.py",
    "myapi/tests/test_models.py",
    "myapi/tests/test_views.py",
    "myapi/tests/test_tasks.py",
]

# Create folders
for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Create files
for file in files:
    file_path = os.path.join(base_path, file)
    with open(file_path, "w") as f:
        f.write("")

# Return the structure for confirmation
folders, files
