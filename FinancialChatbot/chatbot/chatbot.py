import pandas as pd

# Create a dictionary with our sample financial data
data = {
    'Year': [2023, 2023, 2024, 2024],
    'Quarter': ['Q3', 'Q4', 'Q1', 'Q2'],
    'Revenue': [100000, 110000, 120000, 130000],
    'Net Income': [15000, 17000, 18000, 20000],
    'Expenses': [85000, 93000, 102000, 110000]
}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# --- This is our "Data Analysis" ---
# Calculate total revenue for the last full year (2023)
total_revenue_2023 = df[df['Year'] == 2023]['Revenue'].sum()

# Calculate the change in net income from Q4 2023 to Q2 2024
net_income_q4_2023 = df.loc[(df['Year'] == 2023) & (df['Quarter'] == 'Q4'), 'Net Income'].iloc[0]
net_income_q2_2024 = df.loc[(df['Year'] == 2024) & (df['Quarter'] == 'Q2'), 'Net Income'].iloc[0]
net_income_change = net_income_q2_2024 - net_income_q4_2023

# Find the quarter with the highest expenses
highest_expense_quarter = df.loc[df['Expenses'].idxmax()]

print("Data loaded and analyzed successfully!")
print(df) # Optional: print the dataframe to see it

# --- Chatbot Logic ---

def financial_chatbot():
    """Main function to run the interactive chatbot."""
    print("\n--- Welcome to the Financial Chatbot! ---")
    print("You can ask me about our finances. Type 'quit' to exit.")

    while True:
        # Get user input
        user_query = input("\nYour question: ").strip().lower()

        # Check if the user wants to quit
        if user_query == 'quit':
            print("Thank you for using the Financial Chatbot. Goodbye!")
            break

        # Respond based on predefined queries
        if "total revenue in 2023" in user_query:
            response = f"The total revenue in 2023 was ${total_revenue_2023:,.2f}."
        elif "net income changed" in user_query:
            if net_income_change > 0:
                change_desc = "increased"
            else:
                change_desc = "decreased"
            response = f"Net income has {change_desc} by ${abs(net_income_change):,.2f} since Q4 2023."
        elif "highest expenses" in user_query:
            response = f"The quarter with the highest expenses was {highest_expense_quarter['Quarter']} {highest_expense_quarter['Year']} with ${highest_expense_quarter['Expenses']:,.2f}."
        elif "latest reported net income" in user_query:
            response = f"The latest reported net income (Q2 2024) is ${net_income_q2_2024:,.2f}."
        else:
            response = "Sorry, I can't answer that. Please ask one of the predefined questions."
        
        print(f"Bot: {response}")

# Start the chatbot
if __name__ == "__main__":
    financial_chatbot()