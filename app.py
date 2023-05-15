import os
import random
import re

# Müzik dosyası içindeki müzikleri oku
muzik_dosyasi_klasoru = 'C:\\Users\\ufukc\\Desktop\\kk'
muzikler = os.listdir(muzik_dosyasi_klasoru)

# Sayısal değerlerle başlayan adlardaki sayısal değerleri sil
for i, muzik in enumerate(muzikler):
    dosya_adi, dosya_uzantisi = os.path.splitext(muzik)
    yeni_dosya_adi = re.sub('^\d+', '', dosya_adi) + dosya_uzantisi
    eski_dosya_yolu = os.path.join(muzik_dosyasi_klasoru, muzik)
    yeni_dosya_yolu = os.path.join(muzik_dosyasi_klasoru, yeni_dosya_adi)
    os.rename(eski_dosya_yolu, yeni_dosya_yolu)
    muzikler[i] = yeni_dosya_adi

# Müzikleri rastgele bir şekilde sırala
random.shuffle(muzikler)

# Müziklere rastgele sayılar ekle
for i, muzik in enumerate(muzikler):
    dosya_adi, dosya_uzantisi = os.path.splitext(muzik)
    yeni_dosya_adi = f'{i+1:03d}_{dosya_adi}{dosya_uzantisi}' # örneğin, "001_music.mp3" şeklinde olacak
    eski_dosya_yolu = os.path.join(muzik_dosyasi_klasoru, muzik)
    yeni_dosya_yolu = os.path.join(muzik_dosyasi_klasoru, yeni_dosya_adi)
    os.rename(eski_dosya_yolu, yeni_dosya_yolu)

print('Müzik dosyası içindeki müzikler rastgele bir şekilde sıralandı ve başlarına rastgele sayılar eklendi.')
