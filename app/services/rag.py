from sqlalchemy.orm import Session
from sqlalchemy import text

from app.services.chunker import chunk_text
from app.services.embedding import get_embedding
from app.db.models import DocumentChunk


def retrieve_relevant_chunks(query: str, db: Session, top_k: int = 3):
    query_embedding = get_embedding(query)

    sql = text("""
        SELECT content
        FROM document_chunks
        ORDER BY embedding <-> CAST(:query_embedding AS vector)
        LIMIT :top_k
    """)

    results = db.execute(
        sql,
        {"query_embedding": query_embedding, "top_k": top_k}
    ).fetchall()

    return [r[0] for r in results]


def ingest_document(text: str, db: Session):
    chunks = chunk_text(text)

    for chunk in chunks:
        embedding = get_embedding(chunk)

        db_chunk = DocumentChunk(
            content=chunk,
            embedding=embedding
        )
        db.add(db_chunk)

    db.commit()