from app.db.postgres import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)