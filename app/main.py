from enum import Enum

from fastapi import FastAPI

app = FastAPI()

class ModelNameEnum(str, Enum):
    yaris = "yaris"
    camry = "camry"
    civic = "civic"
    accord = "accord"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelNameEnum):
    if model_name is ModelNameEnum.yaris:
        return {"model_name": model_name, "message": "All new toyota YARiS ATIV!"}

    if model_name.value == "camry":
        return {"model_name": model_name, "message": "New CAMRY the absolute perfection"}
    
    if model_name is ModelNameEnum.civic:
        return {"model_name": model_name, "message": "New CIVIC drive the unrival"}

    return {"model_name": model_name, "message": "The Accord"}