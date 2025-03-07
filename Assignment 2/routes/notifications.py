from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

# Define the Notification Pydantic model
class Notification(BaseModel):
    id: int
    patient_id: str
    type: str  
    message: str  
    sent_at: datetime

router = APIRouter()

# In-memory list to store notifications
notifications = []

# Send a new notification (POST)
@router.post("/notifications/")
async def send_notification(notification: Notification):
    # For now, just append to the list of notifications
    notifications.append(notification)
    # Implement actual notification sending logic (e.g., email or SMS)
    return {"message": "Notification sent", "notification": notification}

# View all notifications (GET)
@router.get("/notifications/")
async def view_notifications():
    if not notifications:
        return {"message": "No notifications found."}
    return notifications

# Delete a notification by ID (DELETE)
@router.delete("/notifications/{notification_id}/")
async def delete_notification(notification_id: int):
    for i, existing_notification in enumerate(notifications):
        if existing_notification.id == notification_id:
            del notifications[i]
            return {"message": "Notification deleted successfully."}
    return {"error": "Notification not found"}
