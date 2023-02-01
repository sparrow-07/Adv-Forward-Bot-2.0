import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", 21818317))
    API_HASH = os.environ.get("API_HASH", "bc6ab154300cc41fe127ca4d658dc75d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6129497914:AAG00QCir0bmwjIYzoHCP5_rRu3xKS9Y9mA") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "5650200786")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://classic:classic@cluster0.skzdeyi.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "AQAXvxJ2peuhZaHzEHreGQuEGuxA_naxzgb6-JUxCOXknjvpwfdxDlyc5ZpGThJ-EeiPN9bXbptVTybQD7E5l_lKCKAgAF2U7XHEddk2DB8TaiIK0FjwCgC2pZOhjI9SfQtJ1ArZXtIozt9XoqfogG1BS8I9DkD37NfJez9h5NbRe11MDV_yZhPicjdTNuRZFlnUhXfM2gs4OWCEmMhSA_6by0Zb-r4hIV6laEvb9ji2V-nleqKM_C6DBNS3-IX4FrfIkpASKHXzYh6BWt0HIe2XQF9nkupCKMLA4VeYgC7Wmxu6cyU1ADnVUFTZcNjkdTY17WvDrSFJs8YOWYdTgxZmAAAAAVlFNcEA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", -1001830106391))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", 'Auto_Frwd_Robot')


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
