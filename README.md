<div align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI">
  
  <h1>🚀 AI Support Copilot (Enterprise-Grade RAG Agent)</h1>
  <p>An intelligent, production-ready AI Support Assistant demonstrating advanced state-of-the-art Generative AI capabilities.</p>
</div>

---

## 💡 The Vision
In a world increasingly driven by unstructured data, standard search isn't enough. **AI Support Copilot** bridges the gap between raw documents and intelligent reasoning. I built this project to demonstrate a deep understanding of modern full-stack engineering combined with cutting-edge Applied AI. 

Whether it's parsing complex PDFs, routing intelligent queries to deterministic agentic tools, or maintaining conversational memory via high-speed caching—this application handles it deterministically and efficiently.

## 🏗️ Technical Architecture
This project implements core logic from scratch to showcase real engineering capabilities.

### 🧠 1. Agentic Routing & Tool Use
Instead of a simple "prompt-in, prompt-out" box, the system features an intelligent **Agent Router**. It dynamically parses user intent to route logic into specialized tools:
- **`summarize`**: Instantly aggregates vector chunks to execute a high-level summary of the knowledge base.
- **`actions`**: Instructs the LLM to extract actionable bullet points. 
- **`rag`**: Uses context-aware vector retrieval to answer specific queries exactly without hallucinating.

### 🔍 2. Advanced RAG (Retrieval-Augmented Generation)
The ingestion pipeline natively supports `.pdf` and `.txt`.
- Data is aggressively chunked using semantic boundaries.
- Context embeddings are generated via OpenAI models.
- Instead of relying on expensive managed Vector DBs, this project uses **PostgreSQL with the `pgvector` extension** to perform high-speed cosine distance similarity search (`<->`) natively at the database layer using SQLAlchemy.

### ⚡ 3. High-Speed Memory & Caching
RAG without context is just standard search. The Copilot maintains sophisticated **session-based conversational memory** backed by **Redis**. 
- Conversation history is serialized, stored, and retrieved in milliseconds.
- Native `ltrim` logic ensures the context window never exceeds LLM token limits, optimizing costs.

### 🎨 4. Beautiful, Vanilla Stack Frontend
Who needs heavy `node_modules` for a sleek UI? The frontend is built using pure **HTML/CSS/Vanilla JS** showcasing:
- **Glassmorphism design** with dynamic CSS gradients and backdrops.
- Asynchronous API handling with intelligent loading and typing states.
- Clean component separation without the bloat of heavy JS frameworks.

### 🐳 5. Containerized Infrastructure
The underlying database and caching instances are containerized via **Docker**. Bringing this entire application's dependent infrastructure to life is as simple as running a single command.

---

## 🛠️ Getting Started 

### Prerequisites
- Docker & Docker Compose
- Python 3.9+
- OpenAI API Key

### 1. Spin up the Infrastructure 
```bash
docker-compose up -d
```
*This boots up PostgreSQL on port 5433 (running pgvector) and Redis on 6379.*

### 2. Setup the Environment
```bash
# Create and activate your virtual environment
python3 -m venv venv
source venv/bin/activate

# Install all backend dependencies
pip install -r requirements.txt

# Setup your Secrets
# -> Create a `.env` file containing: OPENAI_API_KEY=your_key_here
```

### 3. Initialize the Backend
Run the database schema seeder to create the vector schemas, then boot up FastAPI:
```bash
python -m app.db.init_db
uvicorn app.main:app --reload
```

### 4. Boot up the Frontend UI
In a separate terminal, serve the UI logic:
```bash
cd ui
python -m http.server 3000
```
Visit `http://localhost:3000` to interact with the finished product!

---

## 👨‍💻 Why Hire Me?
This architecture proves that I don't just know how to call an API. I deeply understand how to orchestrate **microservices (FastAPI)**, map advanced schemas leveraging **Relational + Vector structures (PostgreSQL)**, maintain high-concurrency state via **in-memory caching (Redis)**, build **intelligent agent flows**, and ship an incredible, frictionless User Experience.

I adapt fast, build scalable systems, and understand the intricate bridge between classic standard Software Engineering and modern Applied Machine Learning. **Let's build something incredible together.**
