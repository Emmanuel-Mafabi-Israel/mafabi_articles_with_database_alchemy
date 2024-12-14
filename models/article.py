# GLORY BE TO GOD,
# ARTICLES SYSTEM - ARTICLE,
# BY ISRAEL MAFABI EMMANUEL

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session
from database.connection import BASE
class Article(BASE):
    # our articles table
    __tablename__:str = "articles"

    # the columns and their respective attributes...
    ArticleID:int  = Column(Integer, primary_key=True, index=True)
    Title:str      = Column(String, nullable=False)
    Content:str    = Column(String, nullable=False)
    AuthorID:int   = Column(Integer, ForeignKey('authors.AuthorID'))
    MagazineID:int = Column(Integer, ForeignKey('magazines.MagazineID'))

    # relationships -> the article connects these two (Author and Magazine 😉)
    author   = relationship("Author")
    magazine = relationship("Magazine")
    
    @classmethod
    def create_article(
        cls, 
        DB:Session, 
        title: str, 
        content: str, 
        author_id: int, 
        magazine_id: int): # -> Article
        # create a new article...
        db_article = cls(Title=title, Content=content, AuthorID=author_id, MagazineID=magazine_id) 
        DB.add(db_article) 
        DB.commit() 
        DB.refresh(db_article) 

        return db_article

    @classmethod
    def get_articles(
        cls, 
        DB:Session):
        # retrieve all the articles...
        return DB.query(cls).all()
    
    def __repr__(self)->str:
        return f"<Article: {self.title}>"