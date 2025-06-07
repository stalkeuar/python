from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/askStatus")
def read_root():
    return JSONResponse(content={"status": "ok"})