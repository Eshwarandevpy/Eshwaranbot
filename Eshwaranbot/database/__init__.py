from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from Eshwaranbot.config import MONGO_DB_URI


MONGODB_CLI = MongoClient(MONGO_DB_URI)
db = MONGODB_CLI.wbb
