# from langchain_ollama import ChatOllama
# from langchain_core.messages import AIMessage, HumanMessage
# from sentence_transformers import SentenceTransformer
# import chromadb
# from chromadb.config import Settings
# import sqlite3
# import numpy as np

# def insert_book_and_author(conn, title, genre, description, year, author_name):
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO books (title, genre, description, year) VALUES (?, ?, ?, ?)', (title, genre, description, year))
#     book_id = cursor.lastrowid
#     cursor.execute('INSERT INTO authors (name, book_id) VALUES (?, ?)', (author_name, book_id))
#     conn.commit()

# def fetch_book_and_author(conn, book_title):
#     cursor = conn.cursor()
#     cursor.execute('SELECT b.title, a.name FROM books b JOIN authors a ON b.id = a.book_id WHERE b.title = ?', (book_title,))
#     return cursor.fetchone()

# def test_functionality():
#     # Initialize components
#     llm = ChatOllama(model="phi3:latest", temperature=0, memory=False)
#     model = SentenceTransformer('all-MiniLM-L6-v2')
#     client = chromadb.PersistentClient(path="/Users/mahassaf004/Desktop/book_store_bot")

#     # Check if collection exists and delete it
#     try:
#         client.delete_collection(name="test_collection")
#     except Exception as e:
#         print(f"Collection deletion error: {e}")

#     # Create a new collection (Remove or comment out if not necessary)
#     # collection = client.create_collection(name="test_collection")

#     # Create a database connection
#     conn = sqlite3.connect('test_books.db')

#     # Create tables for testing
#     create_books_table_sql = """
#     CREATE TABLE IF NOT EXISTS books (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         genre TEXT,
#         description TEXT,
#         year INTEGER
#     );"""

#     create_authors_table_sql = """
#     CREATE TABLE IF NOT EXISTS authors (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         book_id INTEGER NOT NULL,
#         FOREIGN KEY (book_id) REFERENCES books (id)
#     );"""

#     cursor = conn.cursor()
#     cursor.execute(create_books_table_sql)
#     cursor.execute(create_authors_table_sql)

#     # Insert a test book and author
#     insert_book_and_author(conn, 'Mystical Paths', 'Fiction', 'A mystical journey.', 2023, 'Kim Stanley Robinson')

#     # Fetch the book and author details to verify
#     book_and_author = fetch_book_and_author(conn, 'Mystical Paths')
#     print(f"Book and Author: {book_and_author}")

#     # Asking the question about the book and author using the LLM
#     if book_and_author:
#         response_text = f"The author of the book '{book_and_author[0]}' is {book_and_author[1]}."
#     else:
#         question = "Who is the author of the book Mystical Paths?"
#         messages = [HumanMessage(content=question)]
#         response = llm(messages)
#         response_text = response.content
    
#     print(f"LLM Response: {response_text}")

#     # Clean up
#     conn.close()

# if __name__ == '__main__':
#     test_functionality()
