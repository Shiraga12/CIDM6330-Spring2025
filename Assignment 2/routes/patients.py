from fastapi import APIRouter
from pydantic import BaseModel

# Define the Patient Pydantic model
class Patient(BaseModel):
    id: int
    name: str
    email: str
    phone: str

router = APIRouter()

# In-memory list to store patients
patients = []

# Register a new patient (POST)
@router.post("/patients/")
async def create_patient(patient: Patient):
    patients.append(patient)
    return patient

# Get a specific patient by ID (GET)
@router.get("/patients/{patient_id}")
async def get_patient(patient_id: int):
    for patient in patients:
        if patient.id == patient_id:
            return patient
    return {"error": "Patient not found"}

# Get all patients (GET)
@router.get("/patients/")
async def list_patients():
    if not patients:
        return {"message": "No patients found."}
    return patients

# Update an existing patient's details (PUT)
@router.put("/patients/{patient_id}/")
async def update_patient(patient_id: int, patient: Patient):
    for i, existing_patient in enumerate(patients):
        if existing_patient.id == patient_id:
            patients[i] = patient
            return patient
    return {"error": "Patient not found"}

# Remove a patient (DELETE)
@router.delete("/patients/{patient_id}/")
async def remove_patient(patient_id: int):
    for i, existing_patient in enumerate(patients):
        if existing_patient.id == patient_id:
            del patients[i]
            return {"message": "Patient removed successfully."}
    return {"error": "Patient not found"}
