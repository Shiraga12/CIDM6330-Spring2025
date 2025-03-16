from fastapi import APIRouter, Depends
from sqlmodel import SQLModel, Session, Field  # ✅ Ensure Field is imported
from models.database import get_session
from typing import Optional

class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    phone: str

router = APIRouter()

@router.post("/patients/")
async def create_patient(patient: Patient, session: Session = Depends(get_session)):
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient

@router.get("/patients/{patient_id}")
async def get_patient(patient_id: int, session: Session = Depends(get_session)):
    patient = session.get(Patient, patient_id)
    if patient:
        return patient
    return {"error": "Patient not found"}

