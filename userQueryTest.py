from get_books_details import*

def main():
    user_query = input("Enter your query: ")
    results = query_books(user_query,1)

    database = "books.db"
    conn = create_connection(database)

    # Extract book_ids from results
    book_ids = [metadata['book_id'] for metadata_list in results['metadatas'] for metadata in metadata_list]
    
    if not book_ids:
        print("No matching books found.")
        return

    books = fetch_book_details(conn, book_ids)
    authors=fetch_authors(conn,book_ids)

    for book in books:
        print("Title:", book[0])
        print("Genre:", book[1])
        print("Author(s):", authors[book_ids[0]])
        print("Published Year:", book[3])
        print("----------")
        print("Description:", book[2])
        print()


if __name__ == '__main__':
    main()