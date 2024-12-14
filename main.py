# GLORY BE TO GOD,
# ARTICLES SYSTEM,
# BY ISRAEL MAFABI EMMANUEL

import os
import sys
import platform

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

    # a function for creating a new article
    def new_article()->None:
        author_name:str       = input("Enter author's name: ")
        magazine_name:str     = input("Enter magazine's name: ")
        magazine_category:str = input("Enter magazine's category(Science, Tech...): ")
        article_title:str     = input("Enter article Title: ")
        article_content:str   = input("Enter article Content: ")

        author:Author = DB.query(Author).filter(Author.Name == author_name).first()
        if not author:
            # if author does not exist create a new author...
            author:Author = Author.create_author(DB, author_name)

        magazine:Magazine = DB.query(Magazine).filter(Magazine.Name == magazine_name, Magazine.Category == magazine_category).first()
        if not magazine:
            # if magazine does not exist create a new magazine...
            magazine:Magazine = Magazine.create_magazine(DB, magazine_name, magazine_category)

        try:
            Article.create_article(DB, article_title, article_content, author.AuthorID, magazine.MagazineID)
            print("New article created succesfully!")
        except Exception as e:
            print(f"An error occurred while creating the article: {e}")

    # function for viewing the articles
    def view_articles():
        articles:list = Article.get_articles(DB)
        for article in articles:
            print(f"Title: {article.Title}, Content: {article.Content}, Author: {article.author.Name}, Magazine: {article.magazine.Name}")

    # function for retrieving all the authors...
    def view_authors():
        authors:list = Author.get_authors(DB)
        for author in authors:
            print(f"ID: {author.AuthorID}, Name: {author.Name}")

    # function for viewing contributors and contributing authors...
    def contributors():
        magazine_name:str     = input("Enter Magazine name: ")
        magazine_category:str = input("Enter Magazine category(or 'All' for all categories): ")
        magazine              = DB.query(Magazine).filter(Magazine.Name == magazine_name, Magazine.Category == magazine_category).first()
        if not magazine:
            print("Magazine not found!!!")
            return
        
        # get the list of contributing authors...
        contributors = Magazine.get_contributing_authors(DB, magazine.MagazineID)
        if not contributors:
            print("No contributing authors found... especially for this magazine.")

        # otherwise... print the details of each contributing author...
        for contributor in contributors:
            print(f"ID: {contributor.AuthorID}, Name: {contributor.Name}")

    # function for viewing all the magazines logged
    def view_magazines():
        magazines = Magazine.get_magazines(DB)
        for magazine in magazines:
            print(f"ID: {magazine.MagazineID}, Name: {magazine.Name}, Category: {magazine.Category}")

    # function for clearing the screen
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls') # for Windows
        else:
            os.system('clear') # for macOS and Linux

    print("----- Welcome to Mafabi's Articles -----")
    print("Please select an option below:")
    print("1) Create new Article.")
    print("2) View Articles.")
    print("3) View all Authors.")
    print("4) View contributing authors - (starred).")
    print("5) View magazines.")
    print("6) Clear the Screen.")
    print("Otherwise, press any numeric key above or below selections to exit...")

    while True:
        try:
            selection = int(input("Selection option: "))
            if selection == 1:
                new_article()
            elif selection == 2:
                view_articles()
            elif selection == 3:
                view_authors()
            elif selection == 4:
                contributors()
            elif selection == 5:
                view_magazines()
            elif selection == 6:
                clear_screen()
            else:
                print("Goodbye!... :)")
                break
        except ValueError:
            print("Invalid input, please enter a number please...")

if __name__ == "__main__":
    main()