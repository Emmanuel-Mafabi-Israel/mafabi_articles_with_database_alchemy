# GLORY BE TO GOD,
# ARTICLES SYSTEM - CONNECTION SETUP,
# BY ISRAEL MAFABI EMMANUEL

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ensuring the dir always exists... 👊
os.makedirs('database/storage', exist_ok=True)
DB_URL     = "sqlite:///database/storage/magazine.db"
DB_ENGINE  = create_engine(DB_URL) # the database engine...
# local session
LOCAL_SESS = sessionmaker(autocommit=False, autoflush=False, bind=DB_ENGINE)
BASE       = declarative_base() # our base class, where the models will inherit from...

def get_db():
    DB = LOCAL_SESS()
    try:
        yield DB
    finally:
        DB.close()