from fastapi import FastAPI, Depends, Body
from sqlalchemy.orm import Session
import api_model
import os
from db_model import *
from sqlalchemy import create_engine


HOST = "127.0.0.1"
PORT = 7777

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/hello/{name}")
def read_root(name: str):
    return f"hello {name}"

@app.post("/file_path/")
def file_path(data  = Body(), db: Session = Depends(get_db)):
    file = File(
        name = data["name"],
        path = data["path"]
    )
    db.add(file)
    db.commit()
    db.refresh(file)
    print("added ", file)
    return (file)

if __name__ == "__main__":
    import asyncio
    import uvicorn

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(uvicorn.run(app, host=HOST, port=PORT))