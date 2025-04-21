from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

# Kullanıcıdan alacağımız veriyi tanımlıyoruz
class UserRequest(BaseModel):
    user_id: int

@app.get("/")
async def read_root():
    return {"message": "API dokümantasyonuna ulaşmak için '/docs' yolunu ziyaret edebilirsiniz."}

@app.post("/recommend/")
async def recommend_movie(request: UserRequest):
    user_id = request.user_id

    # Kullanıcı kümeleri ve filmleri yükle
    user_clusters = pd.read_csv('data/ml-100k/user_clusters.csv')
    ratings_df = pd.read_csv('data/ml-100k/ratings.csv')
    movies_df = pd.read_csv('data/ml-100k/movies.csv')

    # Kullanıcının ait olduğu kümeyi al
    user_cluster = user_clusters.loc[user_clusters['user_id'] == user_id, 'cluster'].values[0]

    # Aynı kümeye ait diğer kullanıcıları bul
    same_cluster_users = user_clusters[user_clusters['cluster'] == user_cluster]

    # Kullanıcıların izlediği filmleri al
    same_cluster_ratings = ratings_df[ratings_df['user_id'].isin(same_cluster_users['user_id'])]

    # Kullanıcının daha önce izlemediği filmleri öner
    user_rated_movies = ratings_df[ratings_df['user_id'] == user_id]['movie_id'].tolist()
    recommendations = same_cluster_ratings[~same_cluster_ratings['movie_id'].isin(user_rated_movies)]

    # Önerilen filmleri al
    recommended_movies = recommendations['movie_id'].unique()

    # Film bilgilerini ekleyerek önerilen filmleri listele
    recommended_movie_titles = movies_df[movies_df['movie_id'].isin(recommended_movies)]['title'].tolist()

    # Sadece 3 film önerisi verelim
    return {"recommended_movies": recommended_movie_titles[:3]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
