from datetime import datetime, timedelta
from pydantic import BaseModel
import pytz

tz = pytz.timezone("Asia/Tehran")
print(tz)


class Price(BaseModel):
    id: int
    created_at: datetime
    price: str

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda dt: (dt.astimezone(tz)  + timedelta(hours=3, minutes=30) ).strftime("%d/%m/%y-%H:%M")
        }
