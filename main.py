# GLORY BE TO GOD,
# ARTICLES SYSTEM,
# BY ISRAEL MAFABI EMMANUEL

import os
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

    # sanitization done here...
    def sanitize_input(prompt:str, min_length:int = 1)->str:
        while True:
            user_input:str = input(prompt).strip()
            if len(user_input) >= min_length:
                return user_input
            else:
                print(f"Input must be at least {min_length} character(s) looong...")

    # a function for creating a new article
    def new_article()->None:
        print("----- New article ----- ")
        author_name:str       = sanitize_input("Enter author's name: ")
        magazine_name:str     = sanitize_input("Enter magazine's name: ")
        magazine_category:str = sanitize_input("Enter magazine's category(Science, Tech...): ")
        article_title:str     = sanitize_input("Enter article Title: ")
        article_content:str   = sanitize_input("Enter article Content: ")

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
            print(f"Title: {article.Title} | Content: {article.Content} | Author: {article.author.Name} | Magazine: {article.magazine.Name}")

    # function for retrieving all the authors...
    def view_authors():
        authors:list = Author.get_authors(DB)
        for author in authors:
            print(f"ID: {author.AuthorID} | Name: {author.Name}")

    # function for viewing contributors and contributing authors...
    def all_contributors():
        print("----- Contributors ----- ")
        magazine_name:str     = input("Enter Magazine name: ").strip()
        magazine_category:str = input("Enter Magazine category(or 'All' for all categories): ").strip()
        
        if magazine_category.lower() == "all":
            magazines = DB.query(Magazine).filter(Magazine.Name.ilike(magazine_name)).all()
        else: 
            magazines = DB.query(Magazine).filter(Magazine.Name.ilike(magazine_name), Magazine.Category.ilike(magazine_category)).all()
        
        if magazines:
            print(f"All contributors in {magazine_name}: ")
            contributors_set:set = set()
            for magazine in magazines:
                contributors = Magazine.get_contributors(DB, magazine.MagazineID)
                # print(f"Magazine: {magazine.Name}, Category: {magazine.Category}, Contributors: {contributors}") # Debug info
                if contributors:
                    contributors_set.update(contributors)

            if contributors_set:
                for author in contributors_set:
                    print(f"Author ID: {author.AuthorID} | Name: {author.Name}")
            else:
                print("No contributors found...")
        else:
            print("Magazine not found...")

    # get the starred contributors ⭐⭐⭐
    def starred_contributors():
        print("----- Starred Contributors -----")
        magazine_name:str     = input("Enter Magazine name: ").strip()
        magazine_category:str = input("Enter Magazine category(or 'All' for all categories): ").strip()

        if magazine_category.lower() == "all":
            magazines = DB.query(Magazine).filter(Magazine.Name.ilike(magazine_name)).all()
        else: 
            magazines = DB.query(Magazine).filter(Magazine.Name.ilike(magazine_name), Magazine.Category.ilike(magazine_category)).all()
        
        if magazines:
            print(f"All starred contributors in {magazine_name} - who have contributed more than twice: ")
            starred_set:set = set()
            for magazine in magazines:
                starred = Magazine.get_starred_authors(DB, magazine.MagazineID)
                # print(f"Magazine: {magazine.Name}, Category: {magazine.Category}, Contributors: {starred}") # Debug info
                if starred:
                    starred_set.update(starred)

            if starred_set:
                for author in starred_set:
                    print(f"Author ID: {author.AuthorID} | Name: {author.Name} ⭐⭐⭐")
            else:
                print("No starred contributors found...")
        else:
            print("Magazine not found...")

    # function for viewing all the magazines logged
    def view_magazines():
        magazines = Magazine.get_magazines(DB)
        for magazine in magazines:
            print(f"ID: {magazine.MagazineID} | Name: {magazine.Name} | Category: {magazine.Category}")

    # function for clearing the screen
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls') # for Windows
        else:
            os.system('clear') # for macOS and Linux

    print("----- Welcome to Mafabi's Articles -----")
    def menu():
        print("Please select an option below:")
        print("1) Create new Article.")
        print("2) View Articles.")
        print("3) View all Authors.")
        print("4) View contributions - all, for specific magazine.")
        print("5) View starred authors - contributing authors.")
        print("6) View magazines.")
        print("7) Clear the Screen.")
        print("Otherwise, press any numeric key above or below selections to exit...")

    while True:
        menu()
        try:
            selection = int(input("Selection option: "))
            if selection ==   1:
                new_article()
            elif selection == 2:
                view_articles()
            elif selection == 3:
                view_authors()
            elif selection == 4:
                all_contributors()
            elif selection == 5:
                starred_contributors()
            elif selection == 6:
                view_magazines()
            elif selection == 7:
                clear_screen()
            else:
                print("Goodbye!... :)")
                break
        except ValueError:
            print("Invalid input, please enter a number.")

if __name__ == "__main__":
    main()