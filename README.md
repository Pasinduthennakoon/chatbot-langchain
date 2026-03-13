# FastAPI LangChain Gemini Chatbot (Dockerized)

A conversational AI API built using **FastAPI**, **LangChain**, and **Google Gemini (Gemini 2.5 Flash)**.
The application is containerized using **Docker**, making it easy to deploy and run in any environment.

This project demonstrates how to build a simple **LLM-powered chatbot backend** with conversation context using LangChain.

---

# Features

* FastAPI REST API
* Google Gemini LLM integration
* LangChain prompt pipeline
* Conversation history support
* Environment variable management
* Docker containerization
* Easy local deployment

---

# Tech Stack

* Python
* FastAPI
* LangChain
* Google Gemini API
* Docker
* Uvicorn
* Pydantic
* python-dotenv

---

# Project Structure

```text
chatbot-langchain/
│
├── app.py              # FastAPI application
├── chain.py            # LangChain pipeline
├── config.py           # Environment configuration
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env
└── README.md
```

---

# How It Works

1. The user sends a question to the `/ask` endpoint.
2. FastAPI receives the request.
3. LangChain formats the prompt and includes previous conversation history.
4. The prompt is sent to **Gemini 2.5 Flash**.
5. The model generates a response.
6. The response is returned as JSON.

---

# Local Installation (Without Docker)

## Clone the Repository

```bash
git clone https://github.com/Pasinduthennakoon/chatbot-langchain.git
cd chatbot-langchain
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

You can obtain an API key from:

https://ai.google.dev/

---

# Run the Application

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# Docker Setup

This project is fully containerized using Docker.

---

# Build Docker Image

```bash
docker build -t langchain-chatbot .
```

---

# Run Docker Container

```bash
docker run --env-file .env -p 8000:8000 langchain-chatbot
```

The API will be available at:

```
http://localhost:8000
```

---

# API Documentation

FastAPI automatically provides Swagger documentation.

Open in your browser:

```
http://localhost:8000/docs
```

---

# API Endpoint

### POST `/ask`

Send a question to the chatbot.

Request

```json
{
  "question": "What is machine learning?"
}
```

Response

```json
{
  "response": "Machine learning is a branch of artificial intelligence that enables systems to learn from data."
}
```

---

# Example Request

Using curl:

```bash
curl -X POST http://localhost:8000/ask \
-H "Content-Type: application/json" \
-d '{"question":"Explain deep learning"}'
```

---

# Security Note

Never commit your `.env` file to GitHub.

Add this to `.gitignore`:

```
.env
```

---

# Future Improvements

* Session-based conversation memory
* Streaming responses
* Chat UI frontend
* Vector database (RAG)
* Authentication
* Cloud deployment

---

# Author

Pasindu Thennakoon

AI / Machine Learning Student
Interested in AI systems, LLM applications, and backend AI infrastructure.
