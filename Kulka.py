import pygame
import os.path
import random
from pygame.math import Vector2 as V2
from Platforma import Platforma
from klocek import Klocek
import json

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
MAX_PREDKOSC_KULKI = 15
FOLDER = os.path.dirname(__file__)
class Kulka(pygame.sprite.Sprite):
    def __init__(self,wybor):
        super().__init__()
        self.obraz = pygame.image.load(FOLDER+"/grafika/ball.png")
        self.rect = self.obraz.get_rect()
        self.r = 16
        self.zycia = 5
        self.Poziom = 0
        self.punkty = 0
        if wybor == "2":
            self.file_name = input("Nazwa pliku na ta gre: ")
            self.file = open("saves/"+self.file_name, 'a')
        
        if wybor == "3":
            self.file_name = input("Nazwa pliku z gra: ")
            self.file = open("saves/"+self.file_name, 'r')
            self.read_content = self.file.read()
            self.read_content = json.loads(self.read_content)
            self.zycia = self.read_content["lives"]
            self.Poziom = self.read_content["level"]
            self.punkty = self.read_content["points"]

        self.data = {
        "points":0,
        "lives":5,
        "level":0
        }
        self.przegrana = False
        self.zresetuj_pozycje()
    def zresetuj_pozycje(self):
        self.rect = self.obraz.get_rect(
            center = V2(SZEROKOSC_EKRANU/2,WYSOKOSC_EKRANU-140)
        )
        self.kat_nachylenia=random.randint(-20,20)
        self.wektor = V2(0,-13)
        self.wektor.rotate_ip(self.kat_nachylenia)
        self.przegrana = False
    def aktualizuj(self,szybkosc,FPS):
        y,x = self.wektor/3
        self.rect.move_ip((y/((FPS//(15/8))/32))*szybkosc,(x/((FPS//(15/8))/32))*szybkosc)
    def sprawdz_kolizje(self,platforma:Platforma,klocki):
        # krawedzie ekranu
        if self.rect.left < 0:
            self.wektor.x *= -1
            pygame.mixer.init()
            pygame.mixer.music.load("audio/sciana.mp3")
            pygame.mixer.music.play()
        if self.rect.right > SZEROKOSC_EKRANU:
            self.wektor.x *= -1
            pygame.mixer.init()
            pygame.mixer.music.load("audio/sciana.mp3")
            pygame.mixer.music.play()
        if self.rect.top < 0:
            self.wektor.y *= -1
            pygame.mixer.init()
            pygame.mixer.music.load("audio/sciana.mp3")
            pygame.mixer.music.play()
        if self.rect.bottom > WYSOKOSC_EKRANU:
            self.file = open("saves/"+self.file_name, 'w')
            self.data["lives"] -= 1
            self.file.write(json.dumps(self.data))
            self.file.close()
            self.przegrana = True
        # kolizja z platforma
        if self.rect.colliderect(platforma.rect):
            self.wektor.y *= -1

            pygame.mixer.init()
            pygame.mixer.music.load("audio/platform1.mp3")
            pygame.mixer.music.play()
            
            srodekKulki = self.rect.centerx
            pozycjaPlatformy = platforma.rect.x

            pozKulkiWzglPlatformy = srodekKulki - pozycjaPlatformy
            szerPlatformy = platforma.rect.width

            pozKulkiOut = pozKulkiWzglPlatformy - (szerPlatformy / 2)

            self.wektor.x += platforma.porusza_sie*5
            
            if pozKulkiOut > MAX_PREDKOSC_KULKI: pozKulkiOut = MAX_PREDKOSC_KULKI
            if pozKulkiOut < -MAX_PREDKOSC_KULKI : pozKulkiOut = -MAX_PREDKOSC_KULKI

            self.wektor.x += pozKulkiOut

            if self.wektor.x > MAX_PREDKOSC_KULKI : self.wektor.x = MAX_PREDKOSC_KULKI
            if self.wektor.x < -MAX_PREDKOSC_KULKI : self.wektor.x = -MAX_PREDKOSC_KULKI

            #if self.wektor.x > 10: self.wektor.x = 10
            #if self.wektor.x < -10: self.wektor.x = -10
        
        # kolizja z klockami
        for klocek in klocki:
            if self.kolizja_z_klockiem(klocek):
                self.file = open("saves/"+self.file_name, 'w')
                self.data["points"] += 1
                self.file.write(json.dumps(self.data))
                self.file.close()
                klocek.uderzenie()
                pygame.mixer.init()
                pygame.mixer.music.load("audio/klocek.mp3")
                pygame.mixer.music.play()
                self.punkty += 1
    def kolizja_z_klockiem(self,klocek):
        dystans_x = abs(self.rect.centerx - klocek.rect.centerx) - klocek.rect.w / 2
        dystans_y = abs(self.rect.centery - klocek.rect.centery) - klocek.rect.h / 2
        if dystans_x < self.r and dystans_y < self.r:
            if dystans_x < dystans_y:
                self.wektor.y *= -1
            else:
                self.wektor.x *= -1
            return True
        return False