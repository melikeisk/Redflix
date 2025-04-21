import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Verileri oku
ratings_df = pd.read_csv('data/ml-100k/ratings.csv')

# User-Item matrix oluştur (Her satırda bir kullanıcı, her sütunda bir film)
user_item_matrix = ratings_df.pivot_table(index='user_id', columns='movie_id', values='rating')

# NaN değerleri 0 ile doldur
user_item_matrix = user_item_matrix.fillna(0)

# Veriyi ölçeklendir
scaler = StandardScaler()
user_item_matrix_scaled = scaler.fit_transform(user_item_matrix)

# KMeans modeli ile kümeleri oluştur
kmeans = KMeans(n_clusters=5, random_state=42)  # 5 küme öneriyoruz
kmeans.fit(user_item_matrix_scaled)

# Kullanıcıları hangi kümeye atadıklarını göster
user_item_matrix['cluster'] = kmeans.labels_

# Kullanıcı kümelerini inceleyelim
print(user_item_matrix[['cluster']].head())

# Kümelere göre her kullanıcıya ait grubu kaydedelim
user_item_matrix.to_csv('data/ml-100k/user_clusters.csv')
