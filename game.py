import pygame
import random

pygame.init()

# Renkler
siyah = (0, 0, 0)
koyu_yeşil = (0, 128, 0)
mavi = (0, 0, 255)
kırmızı = (213, 50, 80)
beyaz = (255, 255, 255)

# Ekran boyutları
genişlik = 600
yükseklik = 400
ekran = pygame.display.set_mode((genişlik, yükseklik))
pygame.display.set_caption("Kıvrılan Yılan - Wrap Around")

# Yılan ayarları
yılan_parça_genişliği = 10
yılan_parça_yüksekliği = 10
yılan_hızı = 15

saat = pygame.time.Clock()

# Skor yazdırma fonksiyonu
font = pygame.font.SysFont(None, 35)

def skoru_yaz(sk):
    değer = font.render("Skor: " + str(sk), True, beyaz)
    skor_x = genişlik // 2 - değer.get_width() // 2  # Skoru ekranın ortasında hizalama
    ekran.blit(değer, [skor_x, 10])

# Yılanı çizme fonksiyonu
def yılanı_çiz(parçalar):
    for parça in parçalar:
        pygame.draw.rect(ekran, koyu_yeşil, [parça[0], parça[1], yılan_parça_genişliği, yılan_parça_yüksekliği])

# Oyun fonksiyonu
def oyun():
    x = genişlik // 2
    y = yükseklik // 2
    x_değişim = yılan_parça_genişliği
    y_değişim = 0

    yılan_parçalar = []
    yılan_uzunluğu = 3

    yem_boyutu = yılan_parça_genişliği
    yem_x = round(random.randrange(0, genişlik - yem_boyutu) / yem_boyutu) * yem_boyutu
    yem_y = round(random.randrange(0, yükseklik - yem_boyutu) / yılan_parça_yüksekliği) * yılan_parça_yüksekliği

    oyun_bitti = False

    while not oyun_bitti:
        for etkinlik in pygame.event.get():
            if etkinlik.type == pygame.QUIT:
                oyun_bitti = True
            elif etkinlik.type == pygame.KEYDOWN:
                if etkinlik.key == pygame.K_LEFT and x_değişim == 0:
                    x_değişim = -yılan_parça_genişliği
                    y_değişim = 0
                elif etkinlik.key == pygame.K_RIGHT and x_değişim == 0:
                    x_değişim = yılan_parça_genişliği
                    y_değişim = 0
                elif etkinlik.key == pygame.K_UP and y_değişim == 0:
                    y_değişim = -yılan_parça_yüksekliği
                    x_değişim = 0
                elif etkinlik.key == pygame.K_DOWN and y_değişim == 0:
                    y_değişim = yılan_parça_yüksekliği
                    x_değişim = 0

        # Hareket
        x += x_değişim
        y += y_değişim

        # Wrap-around: ekran dışına çıkan yılan diğer taraftan gelsin
        if x >= genişlik:
            x = 0
        elif x < 0:
            x = genişlik - yılan_parça_genişliği
        if y >= yükseklik:
            y = 0
        elif y < 0:
            y = yükseklik - yılan_parça_yüksekliği

        ekran.fill(siyah)  # Arka plan siyah

        # Yem çiz
        pygame.draw.rect(ekran, mavi, [yem_x, yem_y, yem_boyutu, yem_boyutu])  # Yem mavi

        # Yeni parça ekle
        yeni_parça = [x, y]
        yılan_parçalar.append(yeni_parça)

        # Yılanın boyutunu ayarla
        if len(yılan_parçalar) > yılan_uzunluğu:
            del yılan_parçalar[0]

        # Kafanın kendine çarpmasını kontrol et
        for parça in yılan_parçalar[:-1]:
            if parça == yeni_parça:
                oyun_bitti = True

        # Yılanı çiz
        yılanı_çiz(yılan_parçalar)

        # Skor yazdır
        skoru_yaz(yılan_uzunluğu - 3)

        # Yem yedi mi kontrol et
        if x == yem_x and y == yem_y:
            yılan_uzunluğu += 1
            yem_x = round(random.randrange(0, genişlik - yem_boyutu) / yem_boyutu) * yem_boyutu
            yem_y = round(random.randrange(0, yükseklik - yem_boyutu) / yılan_parça_yüksekliği) * yılan_parça_yüksekliği

        # Ekranı güncelle
        pygame.display.update()

        # Yılanın hızını ayarla
        saat.tick(yılan_hızı)

    # Oyun bittiğinde ekranı göster
    font_large = pygame.font.SysFont(None, 60)
    mesaj = font_large.render("Oyun Bitti!", True, kırmızı)
    ekran.blit(mesaj, [genişlik // 3, yükseklik // 3])
    pygame.display.update()
    pygame.time.delay(2000)

    pygame.quit()

oyun()
