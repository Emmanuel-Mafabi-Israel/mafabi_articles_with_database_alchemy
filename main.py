# GLORY BE TO GOD,
# ARTICLES SYSTEM,
# BY ISRAEL MAFABI EMMANUEL

from database.setup import create_tables
from database.connection import get_db
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def main():
    # initialize the database and create the tables...
    create_tables()
    # create the session - a new db session
    # a database session generator
    DB = next(get_db())

    # create a new article
    def new_article():
        author_name:str       = input("Enter author's name: ")
        magazine_name:str     = input("Enter magazine's name: ")
        magazine_category:str = input("Enter magazine's category(Science, Tech...): ")
        article_title:str     = input("Enter article Title: ")
        article_content:str   = input("Enter article Content: ")


    print("----- Welcome to Mafabi's Articles -----")
    print("Please select an option below:")
    print("1) Create new Article.")
    print("2) View Articles.")
    print("3) View all Authors.")
    print("4) View contributing authors - (starred).")
    print("5) View magazines.")
    print("Otherwise, press any numeric key above or below selections to exit...")

if __name__ == "__main__":
    main()