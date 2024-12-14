# GLORY BE TO GOD,
# ARTICLES SYSTEM - MAGAZINE,
# BY ISRAEL MAFABI EMMANUEL

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database.connection import BASE
class Magazine(BASE):
    __tablename__:str = "magazines"

    MagazineID:int  = Column(Integer, primary_key=True, index=True)
    Name:str        = Column(String, index=True, nullable=False)
    Category:str    = Column(String, nullable=False)
    
    @classmethod
    def create_magazine(
        cls,
        DB:Session, 
        name:str,
        category:str): # returns -> Magazine
        # create a new magazine - new row
        db_magazine = cls(Name=name, Category=category) 
        DB.add(db_magazine) 
        DB.commit() 
        DB.refresh(db_magazine) 

        return db_magazine

    @classmethod
    def get_magazines(
        cls,
        DB:Session)->list: 
        return DB.query(cls).all()
    
    def __repr__(self)->str:
        return f"<Magazine: {self.name}>"