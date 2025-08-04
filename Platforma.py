import pygame
import os.path

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
FOLDER = os.path.dirname(__file__)

class Platforma(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load(FOLDER+"/grafika/pad.png")
        self.zresetuj_pozycje()
        self.porusza_sie = 0
    def zresetuj_pozycje(self):
        self.rect = pygame.Rect(SZEROKOSC_EKRANU/2-70,WYSOKOSC_EKRANU-100,140,30)
    def aktualizuj(self):
        self.porusza_sie = 0
    def ruszaj_platforma(self,wartosc,FPS):
        predkosc = 8
        self.porusza_sie = wartosc
        self.rect.move_ip((wartosc/((FPS//(15/8))/32))*predkosc,0)
        if self.rect.left <= 0:
            self.rect.x = 0
        if self.rect.right >= SZEROKOSC_EKRANU:
            self.rect.x = SZEROKOSC_EKRANU-140