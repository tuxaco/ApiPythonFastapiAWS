from fastapi import FastAPI
from v1.routers import router
from mangum import Mangum

app = FastAPI(titles='FastAPI Tuxaco',description='API to test FastAPI in AWS')
app.include_router(router, prefix='/v1')

@app.get("/")
def read_root():
    return {"Hola Caracolas": "From FastAPI & API Gateway - ATHENEA"}


handler = Mangum(app=app)