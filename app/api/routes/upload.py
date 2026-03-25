import io
import pypdf
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.db.postgres import get_db
from app.services.rag import ingest_document

router = APIRouter()

@router.post("/upload-doc")
async def upload_doc(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    
    if file.filename.lower().endswith('.pdf'):
        reader = pypdf.PdfReader(io.BytesIO(content))
        text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    else:
        text = content.decode("utf-8")

    ingest_document(text, db)

    return {"status": "Document ingested successfully"}