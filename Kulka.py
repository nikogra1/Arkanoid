import pygame
import os.path
import random
from pygame.math import Vector2 as V2
from Platforma import Platforma
from klocek import Klocek

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
MAX_PREDKOSC_KULKI = 15
FOLDER = os.path.dirname(__file__)
class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load(FOLDER+"/grafika/ball.png")
        self.rect = self.obraz.get_rect()
        self.r = 16
        self.punkty = 0
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
    def aktualizuj(self,szybkosc):
        y,x = self.wektor/3
        self.rect.move_ip(y*szybkosc+self.szybkosc1,x*szybkosc+self.szybkosc1)
        if self.szybkosc1 == 1:
            self.szybkosc1 = 0
    def sprawdz_kolizje(self,platforma:Platforma,klocki):
        # krawedzie ekranu
        if self.rect.left < 0:
            self.wektor.x *= -1
        if self.rect.right > SZEROKOSC_EKRANU:
            self.wektor.x *= -1
        if self.rect.top < 0:
            self.wektor.y *= -1
        if self.rect.bottom > WYSOKOSC_EKRANU:
            self.przegrana = True
        # kolizja z platforma
        if self.rect.colliderect(platforma.rect):
            self.wektor.y *= -1
            
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
                klocek.uderzenie()
                self.punkty += 1
                break
    def kolizja_z_klockiem(self,klocek):
        dystans_x = abs(self.rect.centerx - klocek.rect.centerx) - klocek.rect.w / 2
        dystans_y = abs(self.rect.centery - klocek.rect.centery) - klocek.rect.h / 2
        if dystans_x < self.r and dystans_y < self.r:
            if dystans_x < dystans_y:
                self.wektor.y *= -1
                self.szybkosc1 -= 1
            else:
                self.wektor.x *= -1
                self.szybkosc1 -= 1
            return True
        return False