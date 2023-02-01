import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "19134188"))
    API_HASH = os.environ.get("API_HASH", "91587601a5d898e3341b7e4a9e1c2537")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5815403978:AAGPj2rTrHJwk5bo-c7OJI1tcPgeWCQ7lLw")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardvjbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1802523258")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Forward123:Forward123@cluster0.4d1ljfv.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Clus")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQA8CXsiBvAioiev6FI1bzPHS2hLPs46y6eVs8FQ6Y3VKE9n6kWSM8oDVnJdlUTDEtFjO6aJ6fdrHrGodS3TSq91vQhaz67RaNlRWgtjynksMgEpVrbt7zR6s_vz2bdy2Fsy4f-0qQfVyD67KG4oV_Q-07x-HIR-aw2Zwidl4c9laAvFtbgdt0hTtSKS-xoA7ZvcyD2ol3leNTdwv2w59InGgQYNaSPTlmSQ3hoBVK_aZbKcsXCvbNCMKssJXb1_Vwd8VTZvD8HqYLqSFEKFu_lOFAUGWupnvy8tgQziCtxe9gkCNqYf8sd6Zu6aWcwAh25LbX-SQOYc-cSP_70xDkBya3BSegA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001803821951"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "forwardvjbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
