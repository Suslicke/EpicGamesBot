from .models import Base
from sqlalchemy import create_engine
import os
engine = create_engine(f"{os.getenv('SQLALCHEMY_URL')}", future=True, echo=False) # , echo=True
Base.metadata.create_all(engine)