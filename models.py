from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    outages = relationship("Outage", back_populates="device")

class Outage(Base):
    __tablename__ = "outages"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    start_time = Column(DateTime, server_default=func.now())
    end_time = Column(DateTime, nullable=True)
    active = Column(Boolean, default=True)
    device = relationship("Device", back_populates="outages")
