from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class Status(str, Enum):
    basvuruldu= "basvuruldu"
    mulakat= "mulakat"
    reddedildi= "reddedildi"
    kabul= "kabul"


class ApplicationCreate(BaseModel):
    company: str= Field(min_length=1, examples=["Aselsan"])
    position: str= Field(min_length=1, examples=["Yazılım Stajyeri"])
    applied_date: date= Field(examples=["2026-11-17"])
    status: Status= Status.basvuruldu


class Application(ApplicationCreate):
    id: int

class StatusUpdate(BaseModel):
    status: Status    