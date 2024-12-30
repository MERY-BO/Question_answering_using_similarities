from fastapi import FastAPI
from pydantic import BaseModel
from app.retriever import fetch_faq_answer
from app.speech import text_to_speech, speech_to_text

app = FastAPI()

# Define a Pydantic model for the user query
class Query(BaseModel):
    query: str


@app.post("/ask")
async def ask_faq(query: Query):
    """
    Endpoint to accept a user query and return the corresponding FAQ answer.
    """
    user_query = query.query
    answer = fetch_faq_answer(user_query)
    
    # Convert the answer to speech
    text_to_speech(answer)
    return {"answer": answer}

@app.get("/ask-voice")
async def ask_faq_by_voice():
    """
    Endpoint to accept a voice query and return the corresponding FAQ answer.
    """
    # Capture query from speech
    user_query = speech_to_text()

    # If speech-to-text fails, return the error message as a response
    if user_query.startswith("Error") or "could not understand" in user_query:
        return {"error": user_query}
    
    # Fetch the answer
    answer = fetch_faq_answer(user_query)
    
    # Convert the answer to speech
    text_to_speech(answer)
    return {"query": user_query, "answer": answer}
