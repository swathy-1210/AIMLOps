
from fastapi import APIRouter
from schemas.health import get_health
from schemas.predict import api_make_prediction
from typing import Any
from fastapi import Body

router = APIRouter()


@router.get("/api")
def ping():
    return {"message": "pong"}



@router.get("/api/app")
async def read_root():
    return {"message": "Welcome to the Bike Sharing API"}

@router.get("/api/health")
async def health_check():
    return get_health()

@router.post("/api/predict")
async def predict_rentals(payload: Any = Body(None)):
    print(payload)
    return api_make_prediction(payload)