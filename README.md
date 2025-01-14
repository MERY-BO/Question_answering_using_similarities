# FAQ Voice Assistant

This project is a FastAPI-based voice-enabled FAQ assistant. It provides a seamless interface to interact with an FAQ database through both text and voice queries, returning precise answers while supporting speech-to-text and text-to-speech functionalities in French.

## Features

- **Text-based FAQ Querying**: Submit a query via a RESTful API endpoint and get the most relevant FAQ answer.
- **Voice-based FAQ Querying**: Use voice input to query the FAQ system and receive spoken answers.
- **Embeddings for Semantic Search**: Leverages sentence embeddings for efficient and accurate FAQ matching.
- **Web Scraping**: Scrapes FAQs from a specified website and stores them in a SQLite database.
- **Speech-to-Text and Text-to-Speech**: Converts user speech into text queries and provides answers via synthesized speech.

## Directory Structure

```
.
├── app
│   ├── fastapi.py         # FastAPI endpoints
│   ├── model.py           # Embedding generation and loading
│   ├── retriever.py       # FAQ retrieval logic
│   ├── speech.py          # Speech-to-text and text-to-speech functions
├── generate_embeddings.py # Script to generate FAQ embeddings
├── scrape_and_store.py    # Script to scrape FAQs and store them in the database
└── database
    └── faq.db             # SQLite database for storing FAQs
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install additional system dependencies**:
   - For `speech_recognition`: Install microphone drivers.
   - For `pyttsx3`: Ensure text-to-speech dependencies are installed (e.g., `espeak` on Linux).

## Usage

### Step 1: Scrape and Store FAQs

Run the script to scrape FAQs from the specified website and populate the SQLite database:
```bash
python scrape_and_store.py
```

### Step 2: Generate Embeddings

Generate sentence embeddings for the FAQs to enable semantic search:
```bash
python generate_embeddings.py
```

### Step 3: Start the FastAPI Server

Launch the FastAPI server:
```bash
uvicorn app.fastapi:app --reload
```

### Step 4: Interact with the API

- **Text Query**:
  - Endpoint: `POST /ask`
  - Payload:
    ```json
    {
      "query": "What is CHAABI NET?"
    }
    ```

- **Voice Query**:
  - Endpoint: `GET /ask-voice`
  - Speak into the microphone when prompted.

## Key Components

### FastAPI Endpoints (`app/fastapi.py`)
- `POST /ask`: Accepts a text query and returns the most relevant FAQ answer.
- `GET /ask-voice`: Captures a voice query, converts it to text, fetches the answer, and responds with synthesized speech.

### Embedding Management (`app/model.py`)
- **Generate Embeddings**: Encodes FAQ questions into semantic embeddings using SentenceTransformers.
- **Load Embeddings**: Loads pre-computed embeddings for efficient query matching.

### FAQ Retrieval (`app/retriever.py`)
- Finds the most similar FAQ question to the user query using cosine similarity and returns the corresponding answer.

### Speech Functions (`app/speech.py`)
- **Text-to-Speech**: Converts answers into spoken French.
- **Speech-to-Text**: Recognizes French speech and converts it to text.

### FAQ Scraping (`scrape_and_store.py`)
- Extracts FAQ data from a specified website and stores it in a SQLite database.

### Embedding Generation (`generate_embeddings.py`)
- Processes the FAQ data from the database and generates embeddings for all questions.

## Technologies Used

- **FastAPI**: Backend framework for API development.
- **SentenceTransformers**: For semantic similarity and embedding generation.
- **SQLite**: Database for FAQ storage.
- **BeautifulSoup**: Web scraping library.
- **pyttsx3**: Text-to-speech library.
- **SpeechRecognition**: Speech-to-text functionality.

## Prerequisites

- Python 3.8+
- Microphone (for voice queries)
- Internet connection (for web scraping and dependency installation)

## Example Response

**Text Query**:
```json
{
  "query": "What is CHAABI NET?"
}
```
Response:
```json
{
  "answer": "CHAABI NET is a banking service that allows you to manage your accounts online."
}
```