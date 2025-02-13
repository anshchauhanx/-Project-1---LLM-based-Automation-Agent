import os
import json
import requests
import sqlite3
from app.llm import parse_task  # Import LLM for processing

def execute_task(task):
    """Determines and executes the appropriate task."""
    if "count Wednesdays" in task:
        return count_wednesdays("data/dates.txt")
    elif "sort contacts" in task:
        return sort_contacts("data/contacts.json")
    elif "extract email" in task:
        return extract_email("data/email.txt")
    elif "fetch API data" in task:
        return fetch_api_data()
    elif "calculate gold ticket sales" in task:
        return calculate_gold_ticket_sales("data/ticket-sales.db")
    else:
        raise ValueError("Task not recognized")

def count_wednesdays(file_path):
    """Counts the number of Wednesdays in the given file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r") as file:
        dates = file.readlines()

    count = sum(1 for date in dates if "Wednesday" in date)

    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)

    # Write result to file
    output_path = "data/dates-wednesdays.txt"
    with open(output_path, "w") as output_file:
        output_file.write(str(count))

    return f"Wednesdays count: {count}"

def sort_contacts(file_path):
    """Sorts contacts by last name, then first name."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r") as file:
        contacts = json.load(file)

    contacts.sort(key=lambda x: (x["last_name"], x["first_name"]))

    with open("data/contacts-sorted.json", "w") as file:
        json.dump(contacts, file, indent=2)

    return "Contacts sorted successfully!"

def extract_email(file_path):
    """Extracts the sender's email using LLM."""
    with open(file_path, "r") as file:
        email_content = file.read()

    return parse_task(f"Extract the sender's email from this message: {email_content}")

def fetch_api_data():
    """Fetches data from a sample API."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    with open("data/api_response.json", "w") as file:
        json.dump(response.json(), file)
    return "API data fetched!"

def calculate_gold_ticket_sales(db_path):
    """Calculates total sales for 'Gold' ticket type from SQLite database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'")
    total_sales = cursor.fetchone()[0]

    conn.close()

    with open("data/ticket-sales-gold.txt", "w") as file:
        file.write(str(total_sales))

    return f"Total Gold Ticket Sales: {total_sales}"
