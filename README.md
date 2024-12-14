# Magazine Articles Management System

# By Israel Mafabi Emmanuel

## Description

This project is a Magazine Articles Management System built using Python and SQLAlchemy ORM for managing authors, magazines, and articles.

## Project Structure

```shell
project-folder/
│
├── database/
│   ├── storage/
│   │   └── magazine.db
│   ├── connection.py
│   ├── setup.py
│
├── models/
│   ├── article.py
│   ├── author.py
│   └── magazine.py
│
├── relationships/
|   ├── relations.png
|   └── relations.svg
|
└── main.py
```

## Installation

1. **Clone the repository:**

   ```shell
   git clone [mafabi_articles_with_database_alchemy]
   cd project-folder
   ```

2. **Create a virtual environment:**

   ```shell
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```shell
   pip install sqlalchemy
   ```

## Project Files

### database/connection.py

This file handles the database connection setup using SQLAlchemy. It includes creating the necessary database directory, setting up the database URL, creating the engine and session, and providing a function to get the database session.

**Note:** Please ensure you have SQLAlchemy installed as well...

### database/setup.py

This file contains a function to create the database tables using SQLAlchemy models. It imports the necessary components and defines a function to create the tables when executed.

### models/article.py

This file defines the Article model with attributes and relationships. An article is a piece of writing that belongs to a specific author and a magazine.

**Attributes**:

- `ArticleID`: **Unique identifier** for each article.
- `Title`: Title of the article.
- `Content`: Content of the article.
- `AuthorID`: **Foreign key** linking to the author of the article.
- `MagazineID`: **Foreign key** linking to the magazine where the article is published.

**Relationships**:

- An article is connected to an author and a magazine.

**Methods**:

- `create_article`: Creates a new article.
- `get_articles`: Retrieves all articles.

### models/author.py

This file defines the Author model with attributes and relationships. An author writes articles.

- **Attributes**:

  - `AuthorID`: **Unique identifier** for each author.
  - `Name`: Name of the author.

- **Relationships**:

  - An author can write multiple articles.

    *"One to many relationship* 😉*"*

- **Methods**:

  - `create_author`: Creates a new author.
  - `get_author`: Retrieves a single author by ID.
  - `get_authors`: Retrieves all authors.

### models/magazine.py

This file defines the Magazine model with attributes and relationships. A magazine contains articles and has a category, a magazine may cover different topics such as: Health, Technology, Money, etc.

- **Attributes**:

  - `MagazineID`: **Unique identifier** for each magazine.
  - `Name`: Name of the magazine.
  - `Category`: Category of the magazine (e.g., Science, Tech).

- **Relationships**:

  - A magazine can contain multiple articles.

    *"One to many relationship* 😉*"*

- **Methods**:

  - `create_magazine`: Creates a new magazine.
  - `get_magazines`: Retrieves all magazines.
  - `get_starred_authors`: Retrieves authors who have contributed more than twice to a specific magazine.
  - `get_contributors`: Retrieves all authors who have contributed to a specific magazine.

### main.py

This is the main script for interacting with the database through a command-line interface. It provides functions to create articles, view articles, authors, magazines, contributors, and starred authors.

## How to Run the Project

1. **Initialize the database and create tables:**

   ```shell
   python main.py
   ```

2. **Use the menu to interact with the system:**

   - Create new articles
   - View articles
   - View all authors
   - View contributors for a specific magazine
   - View starred authors
   - View magazines
   - Clear the screen

### Sample Usage

1. **Creating a new article:**

   ```shell
   ----- Welcome to Mafabi's Articles -----
   Please select an option below:
   1) Create new Article.
   2) View Articles.
   3) View all Authors.
   4) View contributions - all, for specific magazine.
   5) View starred authors - contributing authors.
   6) View magazines.
   7) Clear the Screen.
   Otherwise, press any numeric key above or below selections to exit...
   Selection option: 1
   ----- New article -----
   Enter author's name: Israel Mafabi Emmanuel
   Enter magazine's name: Science Monthly
   Enter magazine's category(Science, Tech...): Science
   Enter article Title: The Wonders of Space
   Enter article Content: Exploring the vastness of the universe...
   New article created successfully!
   ```

2. **Viewing all the articles:**

   ```shell
   Selection option: 2
   Title: The Wonders of Space | Content: Exploring the vastness of the universe... | Author: Israel Mafabi Emmanuel | Magazine: Science Monthly
   ```

### **Relationships Diagram**

![https://github.com/Emmanuel-Mafabi-Israel/mafabi_articles_with_database_alchemy/blob/main/relationships/relations.png?raw=true]()



### **Enjoy the Project!!!**

Feel free to reach out... 🤭😍😉

Made with Love... 😎

More so, Glory to God!!!