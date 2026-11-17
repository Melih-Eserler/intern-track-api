from fastapi import FastAPI

app = FastAPI(
    title="InternTrack API",
    description="Staj ve iş başvurularını takip eden hafif REST API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "InternTrack API çalışıyor"}