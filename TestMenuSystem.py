from MenuSystem.MenuManager import MenuManager
from Hardware.SH1106 import SH1106LCD
from pygame import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Python Caption')
pygame.mouse.set_visible(0)


lcd = SH1106LCD
menuSystem = MenuManager(lcd)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                MenuManager.upButtonCallback()
            if event.key == K_DOWN:
                MenuManager.downButtonCallback()
            if event.key == K_RETURN:
                MenuManager.setButtonCallback()
            if event.key == K_RSHIFT:
                MenuManager.backButtonCallback()
