from typing import Optional

from fastapi import FastAPI, HTTPException

from app.models import Application, ApplicationCreate, Status, StatusUpdate

app= FastAPI(
    title="InternTrack API",
    description="Staj ve iş başvurularını takip eden hafif REST API",
    version="0.1.0",
)

# Basit bellek içi depolama
applications: list[Application]= []
next_id= 1


@app.get("/")
def root():
    return {"message": "InternTrack API çalışıyor"}


@app.post("/applications", response_model=Application, status_code=201)
def create_application(data: ApplicationCreate):
    global next_id
    new_application= Application(id=next_id, **data.model_dump())
    next_id += 1
    applications.append(new_application)
    return new_application

@app.get("/applications", response_model=list[Application])
def list_applications(status: Optional[Status]= None):
    if status is None:
        return applications
    return [a for a in applications if a.status== status]

@app.patch("/applications/{application_id}/status", response_model=Application)
def update_status(application_id: int, data: StatusUpdate):
    for application in applications:
        if application.id== application_id:
            application.status= data.status
            return application
    raise HTTPException(status_code=404, detail="Başvuru bulunamadı")