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

SAMPLE_LENGTH = 44100*10
SAMPLE_RATE = 220
SAMPLE_WIDTH = float(44100)
FREQUENCY = 1
VOLUME = 1
BIT_DEPTH = 705
CHANNELS = 2
timer = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            pygame.mixer.music.play(-1)
            pygame.time.wait(5000)
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.mixer.quit()
    pygame.display.update()