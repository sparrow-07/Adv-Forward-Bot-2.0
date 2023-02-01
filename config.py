import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "21818317"))
    API_HASH = os.environ.get("API_HASH", "bc6ab154300cc41fe127ca4d658dc75d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6129497914:AAG00QCir0bmwjIYzoHCP5_rRu3xKS9Y9mA") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "5792675265")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://classic:classic@cluster0.skzdeyi.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "Forward_Session")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", -1001830106391))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", Auto_Frwd_Robot)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
