# GLORY BE TO GOD,
# ARTICLES SYSTEM - SETUP, TABLE CREATION,
# BY ISRAEL MAFABI EMMANUEL

from .connection import DB_ENGINE, BASE
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def create_tables()->None:
    # create the database tables...
    BASE.metadata.create_all(bind=DB_ENGINE)

if __name__ == "__main__":
    create_tables()