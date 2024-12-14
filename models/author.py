# GLORY BE TO GOD,
# ARTICLES SYSTEM - AUTHOR,
# BY ISRAEL MAFABI EMMANUEL

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, relationship
from database.connection import BASE
class Author(BASE):
    __tablename__:str = "authors"

    AuthorID:int  = Column(Integer, primary_key=True, index=True)
    Name:str      = Column(String, index=True, nullable=False)
    
    articles = relationship("Article", back_populates="author")

    @classmethod
    def create_author(
        cls,
        DB:Session, 
        name:str):
        db_author = cls(Name=name)
        DB.add(db_author)
        DB.commit()
        DB.refresh(db_author)
        return db_author

    @classmethod
    def get_author(
        cls, 
        DB:Session, 
        author_id:int):
        # return this instance or None...
        # retrieving a single author.
        return DB.query(cls).filter(cls.AuthorID == author_id).first()

    @classmethod
    def get_authors(
        cls, 
        DB:Session)->list:
        # retrieve authors...
        return DB.query(cls).all()
    
    def __repr__(self)->str:
        return f"<Author: {self.name}>"