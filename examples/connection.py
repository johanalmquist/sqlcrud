from sqlmodel import SQLModel, create_engine

import models

engine = create_engine("sqlite:///database.db", echo=False)
SQLModel.metadata.create_all(engine)
