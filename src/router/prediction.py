from fastapi import APIRouter

from src.app.loader import model, data_processor


router = APIRouter

router.get('/predict')
async def predict():
    pass
