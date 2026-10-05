from fastapi import FastAPI

app = FastAPI(title="PrepPilot API")

@app.get("/")
def home():
    return {
        "message": "Welcome to PrepPilot API",
        "status": "running"
    }