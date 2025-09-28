from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime

def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def get_devices(db: Session):
    return db.query(models.Device).all()

def create_outage(db: Session, outage: schemas.OutageCreate):
    db_outage = models.Outage(device_id=outage.device_id)
    db.add(db_outage)
    db.commit()
    db.refresh(db_outage)
    return db_outage

def close_outage(db: Session, outage_id: int):
    outage = db.query(models.Outage).filter(models.Outage.id == outage_id, models.Outage.active==True).first()
    if outage is None:
        return None
    outage.end_time = datetime.utcnow()
    outage.active = False
    db.commit()
    db.refresh(outage)
    return outage
