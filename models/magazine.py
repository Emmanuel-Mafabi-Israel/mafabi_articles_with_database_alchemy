# GLORY BE TO GOD,
# ARTICLES SYSTEM - MAGAZINE,
# BY ISRAEL MAFABI EMMANUEL

from models.author import Author
from models.article import Article

from sqlalchemy import Column, Integer, String, func
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
    def get_starred_authors(
        cls,
        DB:Session,
        magazine_id:int)->list:
        # retrieving all the contributing authors...
        # starred contributors ⭐
        authors:list = DB.query(
            Author
        ).join(
            Article, Article.AuthorID == Author.AuthorID
        ).filter(
            Article.MagazineID == magazine_id
        ).group_by(
            Author.AuthorID
        ).having(
            func.count(Article.ArticleID) > 2
        ).all()

        return authors

    @classmethod
    def get_contributors(
        cls,
        DB:Session,
        magazine_id:int)->list:
        # get the most contributing authors...
        authors:list = DB.query(
            Author
        ).join(
            Article, Article.AuthorID == Author.AuthorID
        ).filter(
            Article.MagazineID == magazine_id
        ).all()

        return authors

    
    def __repr__(self)->str:
        return f"<Magazine: {self.Name}>"