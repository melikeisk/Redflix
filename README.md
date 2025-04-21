# 🎬 Film Öneri Sistemi (KMeans + FastAPI)

Bu proje, kullanıcıların izleme geçmişine göre benzer kullanıcı kümelerini belirleyerek **film önerileri sunan** bir sistemdir. KMeans algoritmasıyla kümeleme yapılır ve FastAPI ile REST servis olarak sunulur.

---

## 🧱 Proje Yapısı

```
project-root/
├── app/
│   ├── api/
│   │   └── recommendations.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   ├── movie.py
│   │   ├── rating.py
│   │   └── user.py
│
├── data/
│   └── ml-100k/
│       ├── ratings.csv
│       ├── movies.csv
│       └── user_clusters.csv
│
├── scripts/
│   ├── create_tables.py
│   ├── kmeans_model.py
│   ├── load_data.py
│   └── recommend_movies.py
│
├── .env
├── .gitignore
├── requirements.txt
├── setup_project.py
└── README.md
```

---

## 📦 Kullanılan Veri Seti

Proje, [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/) veri setini temel alır.

- `ratings.csv`: Kullanıcıların filmlere verdiği puanlar.
- `movies.csv`: Film ID ve başlık bilgileri.
- `user_clusters.csv`: KMeans ile oluşturulmuş kullanıcı kümeleri.

---

## ⚙️ Kurulum

```bash
git clone <repo-url>
cd <repo-folder>
pip install -r requirements.txt
```

### Ortam Değişkenleri (.env)

`.env` dosyası şu şekilde olmalıdır:

```env
DATABASE_URL=sqlite:///./test.db
DEBUG=True
```

> Gerekirse PostgreSQL gibi farklı veritabanlarına uyarlanabilir.

---

## 🚀 Uygulamayı Başlatma

```bash
uvicorn app.main:app --reload
```

> `app/main.py` dosyasında FastAPI uygulaması tanımlanmalı ve router'lar eklenmiş olmalıdır.

---

## 🤖 Nasıl Öneri Alınır?

### `POST /recommend`

Kullanıcının izlediği filmlere göre aynı kümede bulunan diğer kullanıcıların beğendiği ama kullanıcının henüz izlemediği filmlerden öneri yapılır.

#### İstek Gönderme:

```json
POST /recommend
{
  "user_id": 15
}
```

#### curl Örneği:

```bash
curl -X POST http://127.0.0.1:8000/recommend \
     -H "Content-Type: application/json" \
     -d '{"user_id": 15}'
```

#### Yanıt:

```json
{
  "user_id": 15,
  "recommended_movies": [
    "Star Wars (1977)",
    "Toy Story (1995)",
    "Fargo (1996)"
  ]
}
```

> Eğer öneri bulunamazsa uygun bir mesaj dönülür.

---

## 🔧 Script Dosyaları

| Dosya Adı                  | Açıklama                                                 |
|---------------------------|-----------------------------------------------------------|
| `create_tables.py`        | SQLAlchemy modellerinden veritabanı tablolarını oluşturur |
| `load_data.py`            | CSV dosyalarından verileri veritabanına yükler            |
| `kmeans_model.py`         | Kullanıcı-temelli kümeleme işlemi yapar (`user_clusters`) |
| `recommend_movies.py`     | Komut satırından öneri almak için örnek kod               |

---

## 🧠 Öneri Sistemi Nasıl Çalışır?

1. `ratings.csv` içinden kullanıcı-film matrisi oluşturulur.
2. Kullanıcılara ait küme bilgisi `kmeans_model.py` ile hesaplanır (`user_clusters.csv`).
3. Aynı kümeye ait kullanıcıların yüksek puan verdiği ve hedef kullanıcının **henüz izlemediği** filmler önerilir.

---

## ✅ Gereksinimler

```txt
fastapi
uvicorn
pandas
scikit-learn
sqlalchemy
python-dotenv
```

Kurulum için:

```bash
pip install -r requirements.txt
```

---

## 💡 Geliştirme Önerileri

- 🎯 Öneri puanı hesaplama (örneğin ortalama rating bazlı sıralama)
- 🏷️ Film türü, yıl gibi filtreleme seçenekleri ekleme
- 🖥️ Basit bir frontend ile görsel öneri arayüzü

---

## 🙌 Katkı Sağla

Her türlü katkı, hata düzeltmesi ve yeni özellik önerisi için PR gönderebilirsin.

---
