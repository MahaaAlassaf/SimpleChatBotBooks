import chromadb
import sqlite3

from sentence_transformers import SentenceTransformer

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def fetch_book_details(conn, book_ids):
    cur = conn.cursor()
    placeholders = ','.join('?' for _ in book_ids)
    cur.execute(f"SELECT title, genre, description, year FROM books WHERE id IN ({placeholders})", book_ids)
    books = cur.fetchall()
    return books

def fetch_authors(conn, book_ids):
    cur = conn.cursor()
    
    # Prepare placeholders for SQL query
    placeholders = ','.join('?' for _ in book_ids)
    
    # Fetch authors
    cur.execute(f"SELECT book_id, name FROM authors WHERE book_id IN ({placeholders})", book_ids)
    authors = cur.fetchall()
    
    # Organize authors by book_id
    authors_by_book = {}
    
    for book_id, author_name in authors:
        if book_id not in authors_by_book:
            authors_by_book[book_id] = []
        authors_by_book[book_id].append(author_name)
    
    return authors_by_book

def query_books(user_query,k=1):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([user_query])

    client = chromadb.PersistentClient(path="/Users/mahassaf004/Desktop/book_store_bot") 
    collection = client.get_collection(name="book_embeddings")

    # Query the collection with the user's query embedding
    results = collection.query(
        query_embeddings=query_embedding.tolist(), 
        n_results=k
    )
    #print("Query Results:", results)
    return results