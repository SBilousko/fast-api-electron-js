from fastapi import FastAPI, Depends, Body, HTTPException
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

@app.get("/")
def get_all_files(db: Session = Depends(get_db)):
    return db.query(File).all()

@app.post("/file_path/")
def file_path(data = Body(), db: Session = Depends(get_db)):
    file = File(
        name = data["name"],
        path = data["path"]
    )
    db.add(file)
    db.commit()
    return file["path"]

@app.delete("/")
def delete_files(db: Session = Depends(get_db)):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(bind = engine)
    
    # files = db.query(File).all()
    # for file in files:
    #     file_to_delete = db.get(File, file["id"])
    #     db.delete(file_to_delete)
    #     db.commit()
    # return {"ok": True}
    
    # db.execute('''DELETE FROM files''')
    # db.commit()

if __name__ == "__main__":
    import asyncio
    import uvicorn

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(uvicorn.run(app, host=HOST, port=PORT))