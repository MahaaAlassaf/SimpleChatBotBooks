import sqlite3
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
client = chromadb.PersistentClient(path="/Users/mahassaf004/Desktop/book_store_bot") 
collection = client.create_collection("populate_embeddings2")

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def fetch_books(conn):
    """ Fetch all books from the database """
    cur = conn.cursor()
    cur.execute("SELECT id, description FROM books")
    books = cur.fetchall()
    return books

def generate_embeddings(descriptions):
    """ Generate embeddings for a list of descriptions """
    ## Converts book descriptions to embeddings > sentenceTransformer and stores in Chroma
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(descriptions, show_progress_bar=True)
    return embeddings


# def populate_embeddings():
#     # Fetch books from the database
#     books = get_books()
    
#     # Initialize the LangChain embeddings model
#     model = LangChainEmbeddings(model_name='sentence-transformer-model')
    
#     # Generate embeddings for each book's description
#     embeddings = [model.encode(book.description) for book in books]
    
#     # Initialize Chroma vector store
#     vector_store = Chroma()
    
#     # Add embeddings to the vector store
#     for book, embedding in zip(books, embeddings):
#         vector_store.add_embeddings([embedding], metadata={"book_id": book.id, "title": book.title})
    
#     print("Embeddings populated successfully")

# if __name__ == "__main__":
#     populate_embeddings()

# def store_embeddings_in_chroma(embeddings, book_ids):
#     """ Store embeddings in Chroma database """
#     client = chromadb.Client(Settings())
#     collection = client.get_or_create_collection(name="book_embeddings")

#     # Convert embeddings to lists for Chroma
#     vectors = [embedding.tolist() for embedding in embeddings]
#     metadata = [{"book_id": book_id} for book_id in book_ids]
#     ids = [str(book_id) for book_id in book_ids]  

#     # Add embeddings to the collection
#     collection.add(embeddings=vectors, metadatas=metadata, ids=ids)

import numpy as np

def store_embeddings_in_chroma(embeddings, book_ids, batch_size=5000):
    """ Store embeddings in Chroma database with batching """
    # Convert embeddings to lists for Chroma
    vectors = [embedding.tolist() for embedding in embeddings]
    metadata = [{"book_id": book_id} for book_id in book_ids]
    ids = [str(book_id) for book_id in book_ids]  

    # Add embeddings to the collection in batches
    for start in range(0, len(vectors), batch_size):
        end = min(start + batch_size, len(vectors))
        batch_vectors = vectors[start:end]
        batch_metadata = metadata[start:end]
        batch_ids = ids[start:end]

        collection.add(embeddings=batch_vectors, metadatas=batch_metadata, ids=batch_ids)

    print("Embeddings successfully added to Chroma.")

if __name__ == '__main__':
    database = "books.db"
    conn = create_connection(database)
    
    books = fetch_books(conn)
    books = [(book_id, description) for book_id, description in books if description is not None]
    
    descriptions = [book[1] for book in books]
    book_ids = [book[0] for book in books]
    embeddings = generate_embeddings(descriptions)
    store_embeddings_in_chroma(embeddings, book_ids)
    conn.close()

