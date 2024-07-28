# main.py
import pandas as pd
import sqlite3
from database import create_connection, insert_book, insert_author

def main():
    csv_file = "books.csv"
    df = pd.read_csv(csv_file)

    database = "books.db"
    conn = create_connection(database)
    
    for index, row in df.iterrows():
        title = row.get('title', None)
        authors = row.get('authors', None)
        genre = row.get('categories', None)
        description = row.get('description', None)
        year = row.get('published_year', None)
        
        book = (title, genre, description, year)
        book_id = insert_book(conn, book)
        
        if pd.isna(authors):
            insert_author(conn, ("Unknown", book_id))
        else:
            if ";" in authors:
                authors_list = authors.split(";")
                for author in authors_list:
                    author = author.strip()
                    if not author:  
                        author = "Unknown"
                    insert_author(conn, (author, book_id))
            else:
                author = authors.strip()
                if not author:  
                    author = "Unknown"
                insert_author(conn, (author, book_id))

    conn.close()

if __name__ == '__main__':
    main()
