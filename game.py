import pygame
import random

pygame.init()

# Renkler
siyah = (0, 0, 0)
koyu_yeşil = (0, 128, 0)
mavi = (0, 0, 255)
kirmizi = (213, 50, 80)
beyaz = (255, 255, 255)

# Ekran boyutları
genişlik = 600
yükseklik = 400
ekran = pygame.display.set_mode((genişlik, yükseklik))
pygame.display.set_caption("Kıvrılan Yılan - Wrap Around")

# Yılan ayarları
yilan_parça_genişliği = 10
yilan_parça_yüksekliği = 10
yilan_hizi = 15

saat = pygame.time.Clock()

# Fontlar
font = pygame.font.SysFont(None, 35)
font_büyük = pygame.font.SysFont(None, 60)

def skoru_yaz(sk):
    değer = font.render("Skor: " + str(sk), True, beyaz)
    skor_x = genişlik // 2 - değer.get_width() // 2
    ekran.blit(değer, [skor_x, 10])

def yilani_çiz(parçalar):
    for parça in parçalar:
        pygame.draw.rect(ekran, koyu_yeşil, [parça[0], parça[1], yilan_parça_genişliği, yilan_parça_yüksekliği])

def buton_çiz(metin, x, y, genişlik, yükseklik, renk, metin_renk):
    pygame.draw.rect(ekran, renk, [x, y, genişlik, yükseklik])
    yazi = font.render(metin, True, metin_renk)
    yazi_rect = yazi.get_rect(center=(x + genişlik // 2, y + yükseklik // 2))
    ekran.blit(yazi, yazi_rect)
    return pygame.Rect(x, y, genişlik, yükseklik)


def mesaj_göster(mesaj, alt_mesaj=""):
    ekran.fill(siyah)
    metin = font_büyük.render(mesaj, True, kirmizi)
    ekran.blit(metin, [genişlik // 2 - metin.get_width() // 2, yükseklik // 3])
    if alt_mesaj:
        alt = font.render(alt_mesaj, True, beyaz)
        ekran.blit(alt, [genişlik // 2 - alt.get_width() // 2, yükseklik // 2])
    pygame.display.update()

def baslangic_ekrani():
    buton_genişlik = 200
    buton_yükseklik = 60
    buton_x = genişlik // 2 - buton_genişlik // 2
    buton_y = yükseklik // 2

    bekleme = True
    while bekleme:
        ekran.fill(siyah)

        # Başlık
        baslik = font_büyük.render("Yilan Oyunu", True, beyaz)
        ekran.blit(baslik, (genişlik // 2 - baslik.get_width() // 2, yükseklik // 3))

        # Başla butonu
        pygame.draw.rect(ekran, koyu_yeşil, (buton_x, buton_y, buton_genişlik, buton_yükseklik))
        buton_yazi = font.render("BAŞLA", True, beyaz)
        ekran.blit(buton_yazi, (buton_x + buton_genişlik // 2 - buton_yazi.get_width() // 2,
                                buton_y + buton_yükseklik // 2 - buton_yazi.get_height() // 2))

        pygame.display.update()

        for etkinlik in pygame.event.get():
            if etkinlik.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif etkinlik.type == pygame.MOUSEBUTTONDOWN:
                fare_pos = pygame.mouse.get_pos()
                if buton_x < fare_pos[0] < buton_x + buton_genişlik and buton_y < fare_pos[1] < buton_y + buton_yükseklik:
                    bekleme = False


def oyun():
    global yilan_hizi
    x = genişlik // 2
    y = yükseklik // 2
    x_değişim = yilan_parça_genişliği
    y_değişim = 0

    yilan_parçalar = []
    yilan_uzunluğu = 3

    yem_boyutu = yilan_parça_genişliği
    yem_x = round(random.randrange(0, genişlik - yem_boyutu) / yem_boyutu) * yem_boyutu
    yem_y = round(random.randrange(0, yükseklik - yem_boyutu) / yilan_parça_yüksekliği) * yilan_parça_yüksekliği

    oyun_bitti = False

    while not oyun_bitti:
        for etkinlik in pygame.event.get():
            if etkinlik.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif etkinlik.type == pygame.KEYDOWN:
                if etkinlik.key == pygame.K_LEFT and x_değişim == 0:
                    x_değişim = -yilan_parça_genişliği
                    y_değişim = 0
                elif etkinlik.key == pygame.K_RIGHT and x_değişim == 0:
                    x_değişim = yilan_parça_genişliği
                    y_değişim = 0
                elif etkinlik.key == pygame.K_UP and y_değişim == 0:
                    y_değişim = -yilan_parça_yüksekliği
                    x_değişim = 0
                elif etkinlik.key == pygame.K_DOWN and y_değişim == 0:
                    y_değişim = yilan_parça_yüksekliği
                    x_değişim = 0
                elif etkinlik.key == pygame.K_SPACE:  # Space tuşuna basıldığında hızlan
                    yilan_hizi += 10
            elif etkinlik.type == pygame.KEYUP:
                if etkinlik.key == pygame.K_SPACE:  # Space tuşu bırakıldığında eski hıza dön
                    yilan_hizi -= 10

        x += x_değişim
        y += y_değişim

        if x >= genişlik:
            x = 0
        elif x < 0:
            x = genişlik - yilan_parça_genişliği
        if y >= yükseklik:
            y = 0
        elif y < 0:
            y = yükseklik - yilan_parça_yüksekliği

        ekran.fill(siyah)
        pygame.draw.rect(ekran, mavi, [yem_x, yem_y, yem_boyutu, yem_boyutu])

        yeni_parça = [x, y]
        yilan_parçalar.append(yeni_parça)

        if len(yilan_parçalar) > yilan_uzunluğu:
            del yilan_parçalar[0]

        for parça in yilan_parçalar[:-1]:
            if parça == yeni_parça:
                oyun_bitti = True

        yilani_çiz(yilan_parçalar)
        skoru_yaz(yilan_uzunluğu - 3)

        if x == yem_x and y == yem_y:
            yilan_uzunluğu += 1
            yem_x = round(random.randrange(0, genişlik - yem_boyutu) / yem_boyutu) * yem_boyutu
            yem_y = round(random.randrange(0, yükseklik - yem_boyutu) / yilan_parça_yüksekliği) * yilan_parça_yüksekliği

        pygame.display.update()
        saat.tick(yilan_hizi)

    # Oyun bitti ekranı
    while True:
        ekran.fill(siyah)
        mesaj_göster("Oyun Bitti!", f"Skor: {yilan_uzunluğu - 3}")

        # Butonları çiz
        yeniden_başlat_btn = buton_çiz("Yeniden Başlat", genişlik // 2 - 110, yükseklik // 2 + 50, 200, 50, koyu_yeşil,
                                       beyaz)
        cikiş_btn = buton_çiz("Çık", genişlik // 2 - 50, yükseklik // 2 + 120, 100, 40, kirmizi, beyaz)

        pygame.display.update()  # Ekranı yalnızca bir kez güncelle

        while True:  # Fare olaylarını beklemek için bir iç döngü
            for etkinlik in pygame.event.get():
                if etkinlik.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif etkinlik.type == pygame.MOUSEBUTTONDOWN:
                    if yeniden_başlat_btn.collidepoint(etkinlik.pos):
                        oyun()  # Oyunu yeniden başlat
                    elif cikiş_btn.collidepoint(etkinlik.pos):
                        pygame.quit()
                        quit()


# Oyunu başlat
baslangic_ekrani()
oyun()
