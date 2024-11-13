import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://tallerapiflask:tallerapiflask@container-flaskpg:5432/library")
    SQLALCHEMY_TRACK_MODIFICATIONS = False