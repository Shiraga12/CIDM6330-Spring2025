from fastapi import FastAPI
from routes.appointments import router as appointments_router
from routes.patients import router as patients_router
from routes.invoices import router as invoices_router
from routes.notifications import router as notifications_router
app = FastAPI()

# Include the routes
app.include_router(appointments_router)
app.include_router(patients_router)
app.include_router(invoices_router)
app.include_router(notifications_router)
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to MRI Care Manager API"}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
