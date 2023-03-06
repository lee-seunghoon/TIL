from fastapi import FastAPI
from router import ner_router, es_router, schedule_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://0.0.0.0:3000",
        "http://0.0.0.0"
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(ner_router)
app.include_router(es_router)
app.include_router(schedule_router)
