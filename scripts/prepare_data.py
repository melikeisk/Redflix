import pandas as pd
import os

# 📁 Veri yolları
data_dir = "data/ml-100k"
os.makedirs(data_dir, exist_ok=True)

ratings_path = os.path.join(data_dir, "u.data")
movies_path = os.path.join(data_dir, "u.item")

# 📊 u.data dosyasını oku ve ratings.csv olarak kaydet
ratings_columns = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_csv(ratings_path, sep="\t", names=ratings_columns)
ratings.to_csv(os.path.join(data_dir, "ratings.csv"), index=False)

# 🎬 u.item dosyasını oku ve movies.csv olarak kaydet
movies_columns = [
    "movie_id", "title", "release_date", "video_release_date", "IMDb_URL",
    "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy",
    "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror",
    "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
]
movies = pd.read_csv(movies_path, sep="|", names=movies_columns, encoding="latin-1")
movies = movies[["movie_id", "title"]]
movies.to_csv(os.path.join(data_dir, "movies.csv"), index=False)

# 👤 users.csv dosyasını manuel oluştur
users_data = [
    [1, "M", 24, "technician", "85711"],
    [2, "F", 53, "other", "94043"],
    [3, "M", 23, "student", "95223"],
    [4, "F", 33, "educator", "98234"],
    [5, "M", 42, "programmer", "10520"],
    # Gerekirse daha fazla kullanıcı buraya eklenebilir
]
users_columns = ["user_id", "gender", "age", "occupation", "zipcode"]
users_df = pd.DataFrame(users_data, columns=users_columns)
users_df.to_csv(os.path.join(data_dir, "users.csv"), index=False)

print("✅ 'users.csv', 'ratings.csv' ve 'movies.csv' dosyaları başarıyla oluşturuldu.")
