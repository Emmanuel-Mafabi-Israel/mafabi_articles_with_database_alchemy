# GLORY BE TO GOD,
# ARTICLES SYSTEM - MAGAZINE,
# BY ISRAEL MAFABI EMMANUEL

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, relationship
from database.connection import BASE

class Magazine(BASE):
    __tablename__:str = "magazines"

    MagazineID:int  = Column(Integer, primary_key=True, index=True)
    Name:str        = Column(String, index=True, nullable=False)
    Category:str    = Column(String, nullable=False)

    articles = relationship("Article", back_populates="magazine")
    
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
    
    @classmethod
    def get_contributing_authors(
        cls,
        DB:Session,
        magazine_id:int)->list:
        #retrieving all the contributing authors...
        magazine = DB.query(cls).filter(cls.MagazineID == magazine_id).first()
        if not magazine:
            return []
        
        authors:set = set()
        for article in magazine.articles:
            authors.add(article.author)

        return list(authors)
    
    @classmethod
    def get_contributors(
        cls,
        DB:Session,
        category:str = None)->list:
        # get the most contributing authors...
        query = DB.query(cls)
        if category and category.lower() != 'all':
            query = query.filter(cls.Category == category)

        magazines:list = query.all()
        authors:set    = set()
        for magazine in magazines:
            for article in magazine.articles:
                authors.add(article.author)

        return list(authors)

    
    def __repr__(self)->str:
        return f"<Magazine: {self.name}>"