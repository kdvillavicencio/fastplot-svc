from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import data


app = FastAPI()

origins = [
    "*"
    # "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # expose_headers=["*"],
)

app.include_router(data.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
