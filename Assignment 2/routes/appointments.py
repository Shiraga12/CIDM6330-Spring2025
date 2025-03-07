from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

class Appointment(BaseModel):
    id: int
    patient_id: int
    date: datetime
    status: str

router = APIRouter()

appointments = []

@router.post("/appointments/")
async def create_appointment(appointment: Appointment):
    appointments.append(appointment)
    return appointment

@router.get("/appointments/{appointment_id}")
async def get_appointment(appointment_id: int):
    for appointment in appointments:
        if appointment.id == appointment_id:
            return appointment
    return {"error": "Appointment not found"}

# List all appointments (GET)
@router.get("/appointments/")
async def list_appointments():
    if not appointments:
        return {"message": "No appointments found."}
    return appointments

# Update an existing appointment (PUT)
@router.put("/appointments/{appointment_id}/")
async def update_appointment(appointment_id: int, appointment: Appointment):
    for i, existing_appointment in enumerate(appointments):
        if existing_appointment.id == appointment_id:
            appointments[i] = appointment
            return appointment
    return {"error": "Appointment not found"}

# Cancel an appointment (DELETE)
@router.delete("/appointments/{appointment_id}/")
async def cancel_appointment(appointment_id: int):
    for i, existing_appointment in enumerate(appointments):
        if existing_appointment.id == appointment_id:
            del appointments[i]
            return {"message": "Appointment canceled successfully."}
    return {"error": "Appointment not found"}