import math
import wave
import struct
import pygame
import pygame.mixer
import sys
import winsound
from pygame.locals import*

pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 4096)
Clock = pygame.time.Clock()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

sound = pygame.mixer.music.load(open('rubber_biscuit.wav'))

def

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            #sys.quit()
        if event.type == KEYDOWN and event.key == K_UP:
            pygame.mixer.music.play(-1)
            pygame.time.wait(5000)
    pygame.display.update()

pygame.quit()
quit()