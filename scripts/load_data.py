import pandas as pd
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User
from app.models.movie import Movie
from app.models.rating import Rating

import os

# CSV dosyalarının yolu
DATA_DIR = "data/ml-100k"
ratings_df = pd.read_csv(os.path.join(DATA_DIR, "ratings.csv"))
movies_df = pd.read_csv(os.path.join(DATA_DIR, "movies.csv"))

# Veritabanı oturumu
db: Session = SessionLocal()

# 1. Users tablosuna kullanıcı ekle
unique_user_ids = ratings_df["user_id"].unique()
user_objects = [User(id=int(uid), name=f"User{uid}") for uid in unique_user_ids]
db.bulk_save_objects(user_objects)
print(f"✅ {len(user_objects)} kullanıcı eklendi.")

# 2. Movies tablosuna film ekle
movie_objects = [
    Movie(id=int(row["movie_id"]), title=row["title"])
    for _, row in movies_df.iterrows()
]
db.bulk_save_objects(movie_objects)
print(f"✅ {len(movie_objects)} film eklendi.")

# 3. Ratings tablosuna puanları ekle
rating_objects = [
    Rating(
        user_id=int(row["user_id"]),
        movie_id=int(row["movie_id"]),
        rating=int(row["rating"])
    )
    for _, row in ratings_df.iterrows()
]
db.bulk_save_objects(rating_objects)
print(f"✅ {len(rating_objects)} oy eklendi.")

# Commit işlemi
db.commit()
db.close()
print("🎉 Veritabanına tüm veriler başarıyla yüklendi.")
