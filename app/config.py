# app/config.py
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
