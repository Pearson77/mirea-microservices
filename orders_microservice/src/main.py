import uvicorn

from fastapi import FastAPI

from src.api.base_router import base_router

app = FastAPI()
app.include_router(base_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)