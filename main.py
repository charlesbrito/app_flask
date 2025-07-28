from database import models
from database.conexao import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)