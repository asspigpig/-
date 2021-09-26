import pygame as pg
from pygame.locals import *
class screen():
    background={'sunny':pg.image.load("data/background/sunny.png"),'boss':pg.image.load("data/background/boss.png")}
    icon="data/icon/pig.ico"
    mode=pg.display.set_mode((1280,690),RESIZABLE)