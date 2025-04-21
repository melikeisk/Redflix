from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd

# API Router'ı oluştur
router = APIRouter()

# Kullanıcı ID'si için Pydantic modelini oluştur
class UserRequest(BaseModel):
    user_id: int

# Kullanıcıya film önerilerini döndüren fonksiyon
@router.post("/recommend")
def recommend_movies(request: UserRequest):
    # Kullanıcı ID'sini al
    user_id = request.user_id

    # Kümelerle birlikte kullanıcı bilgilerini yükle
    user_clusters = pd.read_csv('data/ml-100k/user_clusters.csv')

    # Kullanıcının ait olduğu kümeyi al
    user_cluster = user_clusters.loc[user_clusters['user_id'] == user_id, 'cluster'].values[0]

    # Aynı kümeye ait diğer kullanıcıları bul
    same_cluster_users = user_clusters[user_clusters['cluster'] == user_cluster]

    # Kullanıcıların izlediği filmleri al
    ratings_df = pd.read_csv('data/ml-100k/ratings.csv')
    same_cluster_ratings = ratings_df[ratings_df['user_id'].isin(same_cluster_users['user_id'])]

    # Kullanıcının daha önce izlemediği filmleri öner
    user_rated_movies = ratings_df[ratings_df['user_id'] == user_id]['movie_id'].tolist()
    recommendations = same_cluster_ratings[~same_cluster_ratings['movie_id'].isin(user_rated_movies)]

    # Eğer öneri listesi boşsa
    if recommendations.empty:
        return {"message": f"User {user_id} için önerilecek film bulunamadı."}

    # Önerilen filmleri al, ilk 3 tanesini alıyoruz
    recommended_movies = recommendations['movie_id'].unique()[:3]

    # Film bilgilerini ekleyerek önerilen filmleri listele
    movies_df = pd.read_csv('data/ml-100k/movies.csv')
    recommended_movie_titles = movies_df[movies_df['movie_id'].isin(recommended_movies)]['title'].tolist()

    # Önerilen filmleri döndür
    return {"user_id": user_id, "recommended_movies": recommended_movie_titles}
