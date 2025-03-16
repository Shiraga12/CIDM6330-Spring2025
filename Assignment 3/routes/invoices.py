from fastapi import APIRouter, Depends
from sqlmodel import SQLModel, Session, Field
from models.database import get_session
from datetime import datetime
from typing import Optional

class Invoice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int
    amount: float
    issued_date: datetime
    paid: bool

router = APIRouter()

@router.post("/invoices/")
async def create_invoice(invoice: Invoice, session: Session = Depends(get_session)):
    session.add(invoice)
    session.commit()
    session.refresh(invoice)
    return invoice

@router.get("/invoices/{invoice_id}")
async def get_invoice(invoice_id: int, session: Session = Depends(get_session)):
    invoice = session.get(Invoice, invoice_id)
    if invoice:
        return invoice
    return {"error": "Invoice not found"}
