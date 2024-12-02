from fastapi import FastAPI
from app.routers import chat #type: ignore
from app.database import Base, engine


# initialize db
Base.metadata.create_all(bind=engine)

app = FastAPI()

#include routers
app.include_router(chat.router, prefix="/api/v1", tags=["chat"]) #type: ignore

@app.get("/")
def root():
    return {"message": "Chat API is running!"}