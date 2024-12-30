from sentence_transformers import SentenceTransformer
import pickle

# Initialize the Sentence-Transformer model
model = SentenceTransformer('paraphrase-mpnet-base-v2')

def generate_embeddings_for_faqs(faq_data):
    """
    This function generates embeddings for the FAQ questions and saves them to a file.
    """
    questions = [faq[1] for faq in faq_data]  # Extract the questions from the FAQ data
    question_embeddings = model.encode(questions)  # Generate embeddings for all questions

    # Save embeddings to a file (or you can store them in the database)
    with open('faq_embeddings.pkl', 'wb') as f:
        pickle.dump((faq_data, question_embeddings), f)

    print("Embeddings saved!")

def load_faq_embeddings():
    """
    Load the saved FAQ data and their embeddings.
    """
    with open('faq_embeddings.pkl', 'rb') as f:
        faqs, question_embeddings = pickle.load(f)
    return faqs, question_embeddings
