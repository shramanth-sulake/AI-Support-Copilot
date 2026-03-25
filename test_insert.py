from app.db.postgres import SessionLocal
from app.services.rag import retrieve_relevant_chunks

db = SessionLocal()

query = "What is FastAPI?"

results = retrieve_relevant_chunks(query, db)

print("\nTop matches:\n")
for r in results:
    print("-", r)