import os

folders = [
    "app/api",
    "app/db",
    "app/models",
    "app/services",
    "data",
    "scripts",
    "models",
    "notebooks"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("✅ Klasör yapısı oluşturuldu.")
