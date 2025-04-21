import pandas as pd

def get_movie_recommendations(user_id: int, k: int = 3) -> list:
    try:
        user_clusters = pd.read_csv('data/ml-100k/user_clusters.csv')
        ratings_df = pd.read_csv('data/ml-100k/ratings.csv')
        movies_df = pd.read_csv('data/ml-100k/movies.csv')

        # Kullanıcının ait olduğu cluster
        user_cluster = user_clusters.loc[user_clusters['user_id'] == user_id, 'cluster'].values[0]
        same_cluster_users = user_clusters[user_clusters['cluster'] == user_cluster]

        # Aynı cluster'daki kullanıcıların puanları
        same_cluster_ratings = ratings_df[ratings_df['user_id'].isin(same_cluster_users['user_id'])]

        # Kullanıcının daha önce izlediği filmleri çıkar
        user_rated_movies = ratings_df[ratings_df['user_id'] == user_id]['movie_id'].tolist()
        recommendations = same_cluster_ratings[~same_cluster_ratings['movie_id'].isin(user_rated_movies)]

        if recommendations.empty:
            return []

        top_movies = recommendations['movie_id'].value_counts().index[:k]
        recommended_titles = movies_df[movies_df['movie_id'].isin(top_movies)]['title'].tolist()
        return recommended_titles

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return []
