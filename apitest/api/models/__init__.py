from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, event
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base

from api import app

engine = create_engine(app.config['DATABASE_URI'],
                       convert_unicode=True,
                       encoding = "utf-8",
                       echo = True
                      )

db_session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine
                                     ))

Model = declarative_base(name='Model')
Model.query = db_session.query_property()

def init_db():
  Model.metadata.create_all(bind=engine)