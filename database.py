from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")

MONGO_DETAILS = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@localhost:27017/{MONGODB_DATABASE}"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client[MONGODB_DATABASE]
portfolio_collection = database.get_collection("portfolios")
