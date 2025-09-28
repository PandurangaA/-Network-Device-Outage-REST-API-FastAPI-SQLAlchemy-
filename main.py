from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, crud, geo_utils
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Network Device & Outage API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/devices/", response_model=schemas.Device)
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    return crud.create_device(db, device)

@app.get("/devices/", response_model=list[schemas.Device])
def list_devices(db: Session = Depends(get_db)):
    return crud.get_devices(db)

@app.get("/devices/geojson")
def devices_geojson(db: Session = Depends(get_db)):
    devices = crud.get_devices(db)
    return geo_utils.to_geojson(devices)

@app.post("/outages/", response_model=schemas.Outage)
def create_outage(outage: schemas.OutageCreate, db: Session = Depends(get_db)):
    return crud.create_outage(db, outage)

@app.patch("/outages/{outage_id}/close", response_model=schemas.Outage)
def close_outage(outage_id: int, db: Session = Depends(get_db)):
    return crud.close_outage(db, outage_id)
