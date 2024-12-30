# retriever.py
import numpy as np
from app.model import load_faq_embeddings
from sentence_transformers import SentenceTransformer

# Initialize the Sentence-Transformer model
model = SentenceTransformer('paraphrase-mpnet-base-v2')

def fetch_faq_answer(query):
    """
    Fetch the most relevant FAQ answer based on the user's query.
    """
    # Load the FAQ data and embeddings
    faqs, question_embeddings = load_faq_embeddings()

    # Generate embedding for the user query
    query_embedding = model.encode([query])[0]

    # Calculate cosine similarity between the query embedding and the stored FAQ question embeddings
    similarities = np.dot(question_embeddings, query_embedding)
    most_similar_idx = np.argmax(similarities)

    # Fetch and return the answer corresponding to the most similar question
    best_match = faqs[most_similar_idx]
    return best_match[2]  # Return the answer from the database
