import os
import json

# Klasördeki JSON dosyalarını bulun
klasor_yolu = 'kfold/fold5/val/json/'  # Klasörünüzün yolunu buraya girin
json_verileri = []

for dosya in os.listdir(klasor_yolu):
    if dosya.endswith('.json'):
        with open(os.path.join(klasor_yolu, dosya), 'r',encoding="utf8") as dosya_oku:
            veri = json.load(dosya_oku)
            json_verileri.append(veri)

# JSON verilerini birleştirin
birlesik_json = json.dumps(json_verileri)

# Birleştirilmiş JSON'u yeni bir dosyaya yazın
with open('kfold/fold5/val/json/birlesik_veri.json', 'w') as cikti_dosyasi:
    cikti_dosyasi.write(birlesik_json)
