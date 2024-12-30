import requests
from bs4 import BeautifulSoup
import sqlite3

# URL for the FAQ page
url = "https://bpnet.gbp.ma/Public/CustomerService/FAQ#"

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Connect to SQLite database
conn = sqlite3.connect('database/faq.db')
cursor = conn.cursor()

# Create a table for FAQs with only questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS faqs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT UNIQUE,
    answer TEXT
)
''')

# Extract FAQs from the webpage
categories = soup.select('li.allQuestion')  # Select all FAQ categories

for category in categories:
    faqs = category.select('ul.services_list > li')  # Select individual FAQs

    for faq in faqs:
        # Extract question and answer
        question = faq.select_one("a.accordion_title2").get_text(strip=True)
        answer_item = faq.select_one("ul.accordion_content2 li")
        answer = answer_item.get_text(strip=True) if answer_item else "Pas de réponse"

        # Insert question and answer into the database
        cursor.execute('''
        INSERT OR IGNORE INTO faqs (question, answer)
        VALUES (?, ?)
        ''', (question, answer))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database with FAQs has been created successfully.")
