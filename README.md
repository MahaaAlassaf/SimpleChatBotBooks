# SimpleChatBotBooks

## Project Goal

The goal of this project is to create a simple chatbot that can manage and retrieve book information from a SQLite database. It leverages the `langchain_ollama` library for natural language understanding and `sentence-transformers` for generating embeddings of book descriptions.

## Features

- Add books and their respective authors to a SQLite database.
- Fetch book and author details based on book titles.
- Use a chatbot to answer questions about books and authors.

## Projecr structure
- README.md
- books.csv                   # CSV file with sample book data
- books.db                    # SQLite database file for storing books and authors
- database.py                 # Script to manage the database connection and operations
- get_books_details.py        # Script to fetch book details from the database
- langchain_bot.py            # Script to handle the chatbot functionality using Langchain and Ollama
- populate_embeddings.py      # Script to generate and store embeddings for book descriptions
- populatedata.py             # Script to populate the database with initial book and author data
- requirements.txt            # List of Python dependencies
- streamlit_app.py            # Streamlit app script to provide a web interface for the chatbot
- testFile.py                 # Script to test various functionalities
- test_functionality.py       # Main script to test the chatbot functionality
  
