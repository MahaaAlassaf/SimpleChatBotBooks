from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage
from get_books_details import create_connection, fetch_book_details, fetch_authors, query_books

# Initialize the ChatOllama instance with the model name
llm = ChatOllama(
    model="phi3:latest",  
    temperature=0,  
    memory=False 
)

# Initialize conversation history
conversation_history = []

def get_response(messages):
    """Get the response from the model."""
    ai_msg = llm.invoke(messages)
    return ai_msg

def process_book_query(query):
    """Process the query to fetch book details."""
    database = "books.db"
    conn = create_connection(database)
    results = query_books(query, 1)
    book_ids = [metadata['book_id'] for metadata_list in results['metadatas'] for metadata in metadata_list]

    if not book_ids:
        return "No matching books found."

    books = fetch_book_details(conn, book_ids)
    authors = fetch_authors(conn, book_ids)

    response = ""
    for book in books:
        response += f"Title: {book[0]}\n"
        response += f"Genre: {book[1]}\n"
        response += f"Author(s): {', '.join(authors[book_ids[0]])}\n"  # Join authors list
        response += f"Published Year: {book[3]}\n"
        response += "----------\n"
        response += f"Description: {book[2]}"

    return response

def main():
    global conversation_history

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        conversation_history.append(("human", user_input))
        messages = [
            ("system", "You are a helpful assistant. If the user query involves searching for books or book-related queries you will formulate that query which will be used to search for books against it and also, append '#search' at the end."),
        ] + conversation_history

       
        response = get_response(messages).content

        
        if '#search' in response:
            
            response = response.replace('#search', '').strip()
            
            book_response = process_book_query(user_input)
            
            print("Assistant:", book_response)
        else:
            
            print("Assistant:", response)
        conversation_history.append(("assistant", response))

if __name__ == "__main__":
    main()
