from fastapi import FastAPI
from database import Base, engine
from models.user import User

app = FastAPI(title="PrepPilot API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Welcome to PrepPilot API",
        "status": "running"
    }