import math
import wave
import struct
import pygame
import sys
import winsound
from pygame.locals import*

pygame.init()
Clock = pygame.time.Clock()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
window.fill((255, 255, 255))
pygame.display.set_caption('Rubber Biscuits')

soundFile = wave.open('rubber_biscuit.wav', 'w')

SAMPLE_LENGTH = soundFile.getnframes()
frames = []
SAMPLE_RATE = 220
SAMPLE_WIDTH = float(44100)
FREQUENCY = 1
VOLUME = 1
BIT_DEPTH = 705
CHANNELS = 2
timer = 0

params = soundFile.getparams()
soundFile.setparams(params)


def get_parameters():
    soundFile.getparams()


def packfile():
    for i in range(0, SAMPLE_LENGTH):
        value = math.sin(2.0 * math.pi*FREQUENCY*(i/SAMPLE_RATE)) * (VOLUME * BIT_DEPTH)
        packaged_value = struct.pack('<h', value)
        for j in range(0, 1):
            value.append(packaged_value)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            winsound.PlaySound('')
            pygame.time.wait(5000)
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.mixer.quit()
    pygame.display.update()