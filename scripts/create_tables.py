import sys
import os

# Proje kök dizinini Python yoluna ekliyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.session import engine
from app.models import user, movie, rating
from app.db.base import Base

print("⏳ Veritabanı tabloları oluşturuluyor...")
Base.metadata.create_all(bind=engine)
print("✅ Veritabanı tabloları oluşturuldu.")
