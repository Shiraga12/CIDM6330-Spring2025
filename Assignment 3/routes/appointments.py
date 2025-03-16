from fastapi import APIRouter, Depends
from sqlmodel import SQLModel, Session, Field  # ✅ Ensure Field is imported
from models.database import get_session
from datetime import datetime
from typing import Optional

class Appointment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # ✅ This should work now
    patient_id: int
    appointment_time: datetime

router = APIRouter()

@router.post("/appointments/")
async def create_appointment(appointment: Appointment, session: Session = Depends(get_session)):
    session.add(appointment)
    session.commit()
    session.refresh(appointment)
    return appointment

@router.get("/appointments/{appointment_id}")
async def get_appointment(appointment_id: int, session: Session = Depends(get_session)):
    appointment = session.get(Appointment, appointment_id)
    if appointment:
        return appointment
    return {"error": "Appointment not found"}
