from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class Portfolio(BaseModel):
    uuid: str
    channel: str
    country: str
    customerCode: str
    items: List[dict] = []
    route: str

    class Config:
        schema_extra = {
            "example": {
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "channel": "online",
                "country": "USA",
                "customerCode": "CUST001",
                "items": [],
                "route": "/home"
            }
        }

# Helper function to convert BSON to a dictionary
def portfolio_helper(portfolio) -> dict:
    return {
        "id": str(portfolio["_id"]),
        "uuid": portfolio["uuid"],
        "channel": portfolio["channel"],
        "country": portfolio["country"],
        "customerCode": portfolio["customerCode"],
        "items": portfolio["items"],
        "route": portfolio["route"],
    }
