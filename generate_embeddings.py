import sqlite3
from app.model import generate_embeddings_for_faqs

def fetch_faq_data():
    # Connect to the SQLite database
    conn = sqlite3.connect("database/faq.db")
    cursor = conn.cursor()

    # Fetch all the FAQ question and answer pairs
    cursor.execute("SELECT id, question, answer FROM faqs")
    faqs = cursor.fetchall()
    conn.close()

    return faqs

# Fetch the data and generate embeddings
faq_data = fetch_faq_data()
generate_embeddings_for_faqs(faq_data)
