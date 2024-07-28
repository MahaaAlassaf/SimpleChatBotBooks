import sqlite3

# Manages the connection to the database.
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_tables(conn):
    create_books_table_sql = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT,
        description TEXT,
        year INTEGER
    );"""
    
    create_authors_table_sql = """
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        book_id INTEGER NOT NULL,
        FOREIGN KEY (book_id) REFERENCES books (id)
    );"""
    
    try:
        cursor = conn.cursor()
        cursor.execute(create_books_table_sql)
        cursor.execute(create_authors_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_book(conn, book):
    sql = ''' INSERT INTO books(title,genre,description,year)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
    return cur.lastrowid

def insert_author(conn, author):
    sql = ''' INSERT INTO authors(name,book_id)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, author)
    conn.commit()
    return cur.lastrowid

def main():
    database = "books.db"
    conn = create_connection(database)
    if conn is not None:
        create_tables(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
