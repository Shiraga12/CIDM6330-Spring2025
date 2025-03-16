from fastapi import APIRouter
from sqlmodel import SQLModel, Field  # ✅ Ensure correct import of SQLModel and Field
from repositories.sql_repo import SQLRepository
from datetime import datetime
from typing import Optional

# Define the Notification model
class Notification(SQLModel, table=True):  # Define the table for Notifications
    id: Optional[int] = Field(default=None, primary_key=True)
    message: str
    timestamp: datetime

# Initialize the router
router = APIRouter()
repository = SQLRepository()  # Your custom repository class

# Endpoint to create a new notification
@router.post("/notifications/")
async def create_notification(notification: Notification):
    return repository.create(notification)

# Endpoint to get a specific notification by ID
@router.get("/notifications/{notification_id}")
async def get_notification(notification_id: int):
    return repository.get(notification_id)

# Endpoint to get all notifications
@router.get("/notifications/")
async def get_all_notifications():
    return repository.get_all()

# Endpoint to delete a notification by ID
@router.delete("/notifications/{notification_id}")
async def delete_notification(notification_id: int):
    return repository.delete(notification_id)
