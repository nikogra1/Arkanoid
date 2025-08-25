import pygame
import os.path
import random
import datetime
import json
from Platforma import Platforma
from Kulka import Kulka
from klocek import Klocek
print("1.Nowa gra bez zapisu")
print("2.Nowa gra z zapisem")
print("3.Wczytaj gre")
wybor = input("")

lista = []
File2 = open("config.json","r")
read_content = File2.read()
read_content = json.loads(read_content)
FPS = read_content["fps"]

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
FOLDER = os.path.dirname(__file__)

pygame.init()
pygame.font.init()

czcionka = pygame.font.SysFont("Comic Sans MS",24)

# poziomy gry
samouczek = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]
poziom2025_08_12 = [ [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]
poziom2025_08_14 = [ [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [4, 4, 4, 4, 1, 4, 4, 4, 4, 4],
            [4, 4, 4, 1, 2, 1, 4, 4, 4, 4],
            [4, 4, 1, 2, 3, 2, 1, 4, 4, 4],
            [4, 4, 4, 1, 2, 1, 4, 4, 4, 4],
            [4, 4, 4, 4, 1, 4, 4, 4, 4, 4],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4] ]
poziom2025_08_10 = [ [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 2, 1, 0, 0, 0, 1],
            [1, 0, 1, 2, 3, 2, 1, 0, 0, 1],
            [1, 0, 0, 1, 2, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1] ]
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
kulka = Kulka(wybor)

klocki = pygame.sprite.Group()

def dodaj_klocki(ekran):
    start = False
    wczytany_poziom = None
    if kulka.Poziom > 6:
        poziom_random = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), 0],
            [0, random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), 0],
            [0, random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), 0],
            [0, random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), random.randint(0,4), 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]
    if str(datetime.date.today()) == "2025-08-10":
        if kulka.Poziom == 1:
            wczytany_poziom = poziom2025_08_10
    elif str(datetime.date.today()) == "2025-08-12":
        if kulka.Poziom == 1:
            wczytany_poziom = poziom2025_08_12
    elif str(datetime.date.today()) == "2025-08-14":
        if kulka.Poziom == 1:
            wczytany_poziom = poziom2025_08_14
    if kulka.Poziom == 0:
        wczytany_poziom = samouczek
    elif kulka.Poziom == 1:
        wczytany_poziom = poziom2
    elif kulka.Poziom == 2:
        wczytany_poziom = poziom3
    elif kulka.Poziom == 3:
        wczytany_poziom = poziom4
    elif kulka.Poziom == 4:
        wczytany_poziom = poziom5
    elif kulka.Poziom == 5:
        wczytany_poziom = poziom6
    elif kulka.Poziom >= 6:
        wczytany_poziom = poziom_random
    
    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(32 + i * 96, 32 + j * 48, wczytany_poziom[j][i])
                klocki.add(klocek)

dodaj_klocki(ekran)

stan_gry = True
deweloper_mode = False
samouczek1 = False
samouczek2 = True
start = False
i = 0

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
    if keys[pygame.K_8]:
        if deweloper_mode == True:
            Poziom = 7
    if keys[pygame.K_9]:
        if deweloper_mode == True:
            Poziom = 8
    if keys[pygame.K_EQUALS] and keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
        if deweloper_mode == True:
            Poziom += 1
    if keys[pygame.K_MINUS]:
        if deweloper_mode == True:
            Poziom -= 1

    if keys[pygame.K_RIGHT]:
        platforma.ruszaj_platforma(2.4,FPS,kulka.szybkosc)
        samouczek1 = True
        start = True
        if samouczek2 == True:
            samouczek2 = False
    if keys[pygame.K_LEFT]:
        platforma.ruszaj_platforma(-2.4,FPS,kilka.szybkosc)
        samouczek1 = True
        start = True
        if samouczek2 == True:
            samouczek2 = False

    if len(klocki.sprites()) == 0:
        kulka.data["level"] += 1
        kulka.Poziom += 1
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()
        dodaj_klocki(ekran)
    if start == True:
        kulka.aktualizuj(2+kulka.punkty/30,FPS)
    klocki.update()
    platforma.aktualizuj()
    kulka.sprawdz_kolizje(platforma,klocki)

    if kulka.przegrana:
        kulka.zycia -= 1
        if kulka.zycia <= 0:
            stan_gry = False
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    ekran.blit(obraz_tla,[0,0])
    for klocek in klocki:
        ekran.blit(klocek.obraz,klocek.rect)
    ekran.blit(platforma.obraz,platforma.rect)
    ekran.blit(kulka.obraz,kulka.rect)

    if samouczek1 == False:
        if kulka.Poziom == 0:
            text0 = czcionka.render("Używaj strzałek aby poruszać platformą",False,(255,255,255))
            ekran.blit(text0,(500,300))
    if samouczek2 == False:
        if i < 60:
            if kulka.Poziom == 0:
                i += 1
                text0 = czcionka.render("Nie pozwól aby piłka wypadła poza mapę!",False,(255,255,255))
                ekran.blit(text0,(500,300))
        if i >= 60 and i < 100:
            if kulka.Poziom == 0:
                i += 1
                text0 = czcionka.render("Miłej gry!",False,(255,255,255))
                ekran.blit(text0,(500,300))

    text = czcionka.render(f"Życia {kulka.zycia}  Punkty: {kulka.punkty}  Poziom: {kulka.Poziom+1}",False,(255,255,255))
    text1 = czcionka.render("D tryb dewelopera",False,(255,255,255))
    text2 =  czcionka.render("Jeżeli jesteś w trybie dewelopera klawiszami: 1,2,3,4,5,6,7,8,9,+,- możesz zmieniać poziomy",False,(255,255,255))
    ekran.blit(text,(16,10))
    ekran.blit(text1,(16,740))
    ekran.blit(text2,(16,770))
    pygame.display.flip()
    zegar.tick(FPS)
pygame.quit()
exit()