import pygame
import os
from pygame.math import Vector2 as V2

class Menu(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.init()
        self.SZEROKOSC = 1024
        self.WYSOKOSC = 800
        self.FOLDER = os.path.dirname(__file__)
        self.obraz = pygame.image.load(self.FOLDER+"/grafika/menu.png")
    def print_menu(self,spacing,writings,screen):
        self.rect = self.obraz.get_rect(
            center = V2(self.SZEROKOSC/2,self.WYSOKOSC-20)
        )
        for i in writings:
            self.rect.move_ip(float(0),spacing)
            screen.blit(self.obraz,self.rect)
            return screen