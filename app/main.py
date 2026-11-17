from fastapi import FastAPI

from app.models import Application, ApplicationCreate

app = FastAPI(
    title="InternTrack API",
    description="Staj ve iş başvurularını takip eden hafif REST API",
    version="0.1.0",
)

# Basit bellek içi depolama
applications: list[Application] = []
next_id = 1


@app.get("/")
def root():
    return {"message": "InternTrack API çalışıyor"}


@app.post("/applications", response_model=Application, status_code=201)
def create_application(data: ApplicationCreate):
    global next_id
    new_application = Application(id=next_id, **data.model_dump())
    next_id += 1
    applications.append(new_application)
    return new_application