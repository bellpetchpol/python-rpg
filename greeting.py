from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def greeting():
    return {"message":"Hello bell"}