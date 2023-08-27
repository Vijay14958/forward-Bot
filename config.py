import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "19134188"))
    API_HASH = os.environ.get("API_HASH", "91587601a5d898e3341b7e4a9e1c2537")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5815403978:AAGvYKSsW-LTWkPynq30f5ISTvPsD7bfnWo")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardvjbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1802523258")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Clus")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001901354395"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "forwardvjbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
