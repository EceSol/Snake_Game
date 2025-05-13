# Snake Game

## Açıklama
Bu proje, klasik yılan oyununu Python ve Pygame kullanarak geliştirilmiş bir versiyonudur.


## Oyun Özellikleri

- **Klasik Yılan Mekaniği:** Yılanı yön tuşları ile kontrol edin, yemleri yiyerek büyütün.
- **Skor Kaydı:** En yüksek skor otomatik olarak `en_yuksek_skor.txt` dosyasına kaydedilir.
- **Bonus Yemler:**
  - **Sarı Yem:** Yılanı 2 parça büyütür (çift puan).
  - **Mavi Yem:** Yılanı 2 parça kısaltır (minimum uzunluk 3).
- **Hız Artışı:** Boşluk tuşuna basılı tutarak yılanı hızlandırabilirsiniz.
- **Wrap Around:** Yılan ekranın bir kenarından çıkar, diğer kenarından tekrar girer.

## Oyunu Başlatma

1. Gerekli kütüphaneleri yükleyin.
```
   pip install pygame
   ```
2. `game.py` dosyasını çalıştırın:
   ```
   python game.py
   ```


## Kontroller

- **Yön Tuşları:** Yılanı hareket ettirir.
- **Boşluk (Space):** Yılanı geçici olarak hızlandırır.
