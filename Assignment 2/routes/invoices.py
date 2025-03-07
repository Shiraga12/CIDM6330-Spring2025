from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

# Define the Invoice Pydantic model
class Invoice(BaseModel):
    id: int
    patient_id: int
    amount: float
    status: str  # e.g., 'paid', 'unpaid', 'pending'

router = APIRouter()

# In-memory list to store invoices
invoices = []

# Generate a new invoice (POST)
@router.post("/invoices/")
async def create_invoice(invoice: Invoice):
    invoices.append(invoice)
    return invoice

# Get a specific invoice by ID (GET)
@router.get("/invoices/{invoice_id}")
async def get_invoice(invoice_id: int):
    for invoice in invoices:
        if invoice.id == invoice_id:
            return invoice
    return {"error": "Invoice not found"}

# List all invoices (GET)
@router.get("/invoices/")
async def list_invoices():
    if not invoices:
        return {"message": "No invoices found."}
    return invoices

# Update an existing invoice (PUT)
@router.put("/invoices/{invoice_id}/")
async def update_invoice(invoice_id: int, invoice: Invoice):
    for i, existing_invoice in enumerate(invoices):
        if existing_invoice.id == invoice_id:
            invoices[i] = invoice
            return invoice
    return {"error": "Invoice not found"}

# Delete an invoice (DELETE)
@router.delete("/invoices/{invoice_id}/")
async def delete_invoice(invoice_id: int):
    for i, existing_invoice in enumerate(invoices):
        if existing_invoice.id == invoice_id:
            del invoices[i]
            return {"message": "Invoice deleted successfully."}
    return {"error": "Invoice not found"}
