import pygame
import os.path
import random
from Platforma import Platforma
from Kulka import Kulka
from klocek import Klocek
lista = []

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
FOLDER = os.path.dirname(__file__)

pygame.init()
pygame.font.init()

czcionka = pygame.font.SysFont("Comic Sans MS",24)

# poziomy gry
poziom1 = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]
poziom2 = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 2, 4, 0, 0, 0, 0],
            [0, 0, 4, 3, 3, 3, 4, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]
poziom3 = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
            [0, 0, 0, 4, 4, 4, 4, 0, 0, 0],
            [0, 0, 4, 4, 4, 4, 4, 4, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]
poziom4 = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
            [0, 0, 0, 4, 4, 4, 4, 0, 0, 0],
            [0, 0, 4, 4, 4, 4, 4, 4, 0, 0],
            [0, 0, 0, 4, 4, 4, 4, 0, 0, 0],
            [0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]
poziom5 = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 3, 3, 3, 3, 0, 0, 0],
            [0, 4, 4, 3, 3, 3, 3, 4, 4, 0],
            [0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]

poziom6 = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 3, 3, 3, 3, 0, 0, 0],
            [0, 4, 4, 3, 3, 3, 3, 4, 4, 0],
            [0, 4, 4, 4, 4, 4, 4, 4, 4, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU,WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load(FOLDER+"/grafika/background.png")
platforma = Platforma()
kulka = Kulka()
zycia = 3
Poziom = 0

klocki = pygame.sprite.Group()

def dodaj_klocki():
    
    wczytany_poziom = None
    if Poziom > 6:
        poziom_random = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), 0],
            [0, random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), 0],
            [0, random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), 0],
            [0, random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]
    if Poziom == 0:
        wczytany_poziom = poziom1
    elif Poziom == 1:
        wczytany_poziom = poziom2
    elif Poziom == 2:
        wczytany_poziom = poziom3
    elif Poziom == 3:
        wczytany_poziom = poziom4
    elif Poziom == 4:
        wczytany_poziom = poziom5
    elif Poziom == 5:
        wczytany_poziom = poziom6
    elif Poziom >= 6:
        wczytany_poziom = poziom_random
    
    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(32 + i * 96, 32 + j * 48, wczytany_poziom[j][i])
                klocki.add(klocek)

dodaj_klocki()

stan_gry = True
deweloper_mode = False

while stan_gry:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            stan_gry = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                stan_gry = False
            
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        zycia = 100
        deweloper_mode = True
    
    if keys[pygame.K_1]:
        if deweloper_mode == True:
            Poziom = 0
    if keys[pygame.K_2]:
        if deweloper_mode == True:
            Poziom = 1
    if keys[pygame.K_3]:
        if deweloper_mode == True:
            Poziom = 2
    if keys[pygame.K_4]:
        if deweloper_mode == True:
            Poziom = 3
    if keys[pygame.K_5]:
        if deweloper_mode == True:
            Poziom = 4
    if keys[pygame.K_6]:
        if deweloper_mode == True:
            Poziom = 5
    if keys[pygame.K_7]:
        if deweloper_mode == True:
            Poziom = 6

    if keys[pygame.K_RIGHT]:
        platforma.ruszaj_platforma(2.4)
    if keys[pygame.K_LEFT]:
        platforma.ruszaj_platforma(-2.4)

    if len(klocki.sprites()) == 0:
        Poziom += 1
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()
        dodaj_klocki()

    kulka.aktualizuj(2+kulka.punkty/25)
    klocki.update()
    platforma.aktualizuj()
    kulka.sprawdz_kolizje(platforma,klocki)

    if kulka.przegrana:
        zycia -= 1
        if zycia <= 0:
            stan_gry = False
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    ekran.blit(obraz_tla,[0,0])
    for klocek in klocki:
        ekran.blit(klocek.obraz,klocek.rect)
    ekran.blit(platforma.obraz,platforma.rect)
    ekran.blit(kulka.obraz,kulka.rect)

    text = czcionka.render(f"Życia {zycia}  Punkty: {kulka.punkty}  Poziom: {Poziom+1} D tryb dewelopera",False,(255,255,255))
    text2 =  czcionka.render("Jeżeli jesteś w trybie dewelopera klawiszami: 1,2,3,4,5,6,7 możesz zmieniać poziomy",False,(255,255,255))
    ekran.blit(text,(16,16))
    ekran.blit(text2,(16,40))
    pygame.display.flip()
    zegar.tick(60)
pygame.quit()
exit()