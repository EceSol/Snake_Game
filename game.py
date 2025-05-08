import pygame
import random

pygame.init()

# Renkler
siyah = (0, 0, 0)
koyu_yesil = (0, 128, 0)
mavi = (0, 0, 255)
kirmizi = (213, 50, 80)
beyaz = (255, 255, 255)

# Ekran boyutları
genislik = 600
yukseklik = 400
ekran = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Kıvrılan Yılan - Wrap Around")

# Yılan ayarları
yilan_parca_genisligi = 10
yilan_parca_yukseligi = 10
yilan_hizi = 15

saat = pygame.time.Clock()

# Fontlar
font = pygame.font.SysFont(None, 35)
font_buyuk = pygame.font.SysFont(None, 60)

# Bonus yemler için başlangıç değerleri
bonus_yem_ekstra_x = round(random.randrange(0, genislik - yilan_parca_genisligi) / yilan_parca_genisligi) * yilan_parca_genisligi
bonus_yem_ekstra_y = round(random.randrange(0, yukseklik - yilan_parca_yukseligi) / yilan_parca_yukseligi) * yilan_parca_yukseligi

bonus_yem_eksi_x = round(random.randrange(0, genislik - yilan_parca_genisligi) / yilan_parca_genisligi) * yilan_parca_genisligi
bonus_yem_eksi_y = round(random.randrange(0, yukseklik - yilan_parca_yukseligi) / yilan_parca_yukseligi) * yilan_parca_yukseligi


def skoru_yaz(sk):
    deger = font.render("Skor: " + str(sk), True, beyaz)
    skor_x = genislik // 2 - deger.get_width() // 2
    ekran.blit(deger, [skor_x, 10])

def yilani_ciz(parcalar):
    for parca in parcalar:
        pygame.draw.rect(ekran, koyu_yesil, [parca[0], parca[1], yilan_parca_genisligi, yilan_parca_yukseligi])

def buton_ciz(metin, x, y, genislik, yukseklik, renk, metin_renk):
    pygame.draw.rect(ekran, renk, [x, y, genislik, yukseklik])
    yazi = font.render(metin, True, metin_renk)
    yazi_rect = yazi.get_rect(center=(x + genislik // 2, y + yukseklik // 2))
    ekran.blit(yazi, yazi_rect)
    return pygame.Rect(x, y, genislik, yukseklik)


def mesaj_goster(mesaj, alt_mesaj=""):
    ekran.fill(siyah)
    metin = font_buyuk.render(mesaj, True, kirmizi)
    ekran.blit(metin, [genislik // 2 - metin.get_width() // 2, yukseklik // 3])
    if alt_mesaj:
        alt = font.render(alt_mesaj, True, beyaz)
        ekran.blit(alt, [genislik // 2 - alt.get_width() // 2, yukseklik // 2])
    pygame.display.update()

def baslangic_ekrani():
    buton_genislik = 200
    buton_yukseklik = 60
    buton_x = genislik // 2 - buton_genislik // 2
    buton_y = yukseklik // 2

    bekleme = True
    while bekleme:
        ekran.fill(siyah)

        # Başlık
        baslik = font_buyuk.render("Yilan Oyunu", True, beyaz)
        ekran.blit(baslik, (genislik // 2 - baslik.get_width() // 2, yukseklik // 3))

        # Başla butonu
        pygame.draw.rect(ekran, koyu_yesil, (buton_x, buton_y, buton_genislik, buton_yukseklik))
        buton_yazi = font.render("BAŞLA", True, beyaz)
        ekran.blit(buton_yazi, (buton_x + buton_genislik // 2 - buton_yazi.get_width() // 2,
                                buton_y + buton_yukseklik // 2 - buton_yazi.get_height() // 2))

        pygame.display.update()

        for etkinlik in pygame.event.get():
            if etkinlik.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif etkinlik.type == pygame.MOUSEBUTTONDOWN:
                fare_pos = pygame.mouse.get_pos()
                if buton_x < fare_pos[0] < buton_x + buton_genislik and buton_y < fare_pos[1] < buton_y + buton_yukseklik:
                    bekleme = False


def oyun():
    global yilan_hizi
    global bonus_yem_ekstra_x, bonus_yem_ekstra_y, bonus_yem_eksi_x, bonus_yem_eksi_y  # Global değişkenleri belirtin

    x = genislik // 2
    y = yukseklik // 2
    x_degisim = yilan_parca_genisligi
    y_degisim = 0

    yilan_parcalar = []
    yilan_uzunlugu = 3

    yem_boyutu = yilan_parca_genisligi
    yem_x = round(random.randrange(0, genislik - yem_boyutu) / yem_boyutu) * yem_boyutu
    yem_y = round(random.randrange(0, yukseklik - yem_boyutu) / yilan_parca_yukseligi) * yilan_parca_yukseligi

    oyun_bitti = False

    while not oyun_bitti:
        for etkinlik in pygame.event.get():
            if etkinlik.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif etkinlik.type == pygame.KEYDOWN:
                if etkinlik.key == pygame.K_LEFT and x_degisim == 0:
                    x_degisim = -yilan_parca_genisligi
                    y_degisim = 0
                elif etkinlik.key == pygame.K_RIGHT and x_degisim == 0:
                    x_degisim = yilan_parca_genisligi
                    y_degisim = 0
                elif etkinlik.key == pygame.K_UP and y_degisim == 0:
                    y_degisim = -yilan_parca_genisligi
                    x_degisim = 0
                elif etkinlik.key == pygame.K_DOWN and y_degisim == 0:
                    y_degisim = yilan_parca_genisligi
                    x_degisim = 0
                elif etkinlik.key == pygame.K_SPACE:  # Space tuşuna basıldığında hızlan
                    yilan_hizi += 10
            elif etkinlik.type == pygame.KEYUP:
                if etkinlik.key == pygame.K_SPACE:  # Space tuşu bırakıldığında eski hıza dön
                    yilan_hizi -= 10

        x += x_degisim
        y += y_degisim

        if x >= genislik:
            x = 0
        elif x < 0:
            x = genislik - yilan_parca_genisligi
        if y >= yukseklik:
            y = 0
        elif y < 0:
            y = yukseklik - yilan_parca_yukseligi

        ekran.fill(siyah)
        pygame.draw.rect(ekran, mavi, [yem_x, yem_y, yem_boyutu, yem_boyutu])

        # Bonus yemleri çiz
        pygame.draw.rect(ekran, koyu_yesil, [bonus_yem_ekstra_x, bonus_yem_ekstra_y, yilan_parca_genisligi, yilan_parca_yukseligi])
        pygame.draw.rect(ekran, kirmizi, [bonus_yem_eksi_x, bonus_yem_eksi_y, yilan_parca_genisligi, yilan_parca_yukseligi])

        yeni_parca = [x, y]
        yilan_parcalar.append(yeni_parca)

        if len(yilan_parcalar) > yilan_uzunlugu:
            del yilan_parcalar[0]

        for parca in yilan_parcalar[:-1]:
            if parca == yeni_parca:
                oyun_bitti = True

        yilani_ciz(yilan_parcalar)
        skoru_yaz(yilan_uzunlugu - 3)

        # Yem yeme kontrolü
        if x == yem_x and y == yem_y:
            yilan_uzunlugu += 1
            yem_x = round(random.randrange(0, genislik - yem_boyutu) / yem_boyutu) * yem_boyutu
            yem_y = round(random.randrange(0, yukseklik - yem_boyutu) / yilan_parca_yukseligi) * yilan_parca_yukseligi

        # Bonus yem yeme kontrolü
        if x == bonus_yem_ekstra_x and y == bonus_yem_ekstra_y:
            yilan_uzunlugu += 2  # Ekstra puan
            bonus_yem_ekstra_x = round(random.randrange(0, genislik - yilan_parca_genisligi) / yilan_parca_genisligi) * yilan_parca_genisligi
            bonus_yem_ekstra_y = round(random.randrange(0, yukseklik - yilan_parca_yukseligi) / yilan_parca_yukseligi) * yilan_parca_yukseligi

        if x == bonus_yem_eksi_x and y == bonus_yem_eksi_y:
            yilan_uzunlugu = max(3, yilan_uzunlugu - 2)  # Puan azalt, minimum 3
            bonus_yem_eksi_x = round(random.randrange(0, genislik - yilan_parca_genisligi) / yilan_parca_genisligi) * yilan_parca_genisligi
            bonus_yem_eksi_y = round(random.randrange(0, yukseklik - yilan_parca_yukseligi) / yilan_parca_yukseligi) * yilan_parca_yukseligi

        pygame.display.update()
        saat.tick(yilan_hizi)

    # Oyun bitti ekranı
    while True:
        ekran.fill(siyah)
        mesaj_goster("Oyun Bitti!", f"Skor: {yilan_uzunlugu - 3}")

        # Butonları çiz
        yeniden_baslat_btn = buton_ciz("Yeniden Başlat", genislik // 2 - 110, yukseklik // 2 + 50, 200, 50, koyu_yesil,
                                       beyaz)
        cikis_btn = buton_ciz("Çık", genislik // 2 - 50, yukseklik // 2 + 120, 100, 40, kirmizi, beyaz)

        pygame.display.update()  # Ekranı yalnızca bir kez güncelle

        while True:  # Fare olaylarını beklemek için bir iç döngü
            for etkinlik in pygame.event.get():
                if etkinlik.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif etkinlik.type == pygame.MOUSEBUTTONDOWN:
                    if yeniden_baslat_btn.collidepoint(etkinlik.pos):
                        oyun()  # Oyunu yeniden başlat
                    elif cikis_btn.collidepoint(etkinlik.pos):
                        pygame.quit()
                        quit()


# Oyunu başlat
baslangic_ekrani()
oyun()
