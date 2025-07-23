# Financial Chatbot Prototype

This project is a simple, command-line AI chatbot for answering basic financial queries based on a predefined dataset.

## How It Works

The chatbot is built using a single Python script (`chatbot.py`).

1.  **Data Handling:** It uses the `pandas` library to create and hold a sample financial DataFrame (revenue, net income, expenses).
2.  **Chatbot Logic:** A `while` loop continuously prompts the user for input.
3.  **Query Matching:** It uses `if-elif-else` statements to check if the user's input contains keywords related to the predefined queries.
4.  **Dynamic Responses:** Responses are generated using f-strings to pull data directly from the pandas DataFrame, ensuring the answers are accurate.

## Predefined Queries

The chatbot can answer the following questions:
- "What was the total revenue in 2023?"
- "How has net income changed since Q4 2023?"
- "Which quarter had the highest expenses?"
- "What is the latest reported net income?"

## Limitations

- The chatbot can **only** respond to the exact predefined queries listed above. It does not understand natural language variations.
- The financial data is hard-coded into the script and is not loaded from an external file.
- The interaction is limited to the command line; there is no graphical user interface.
