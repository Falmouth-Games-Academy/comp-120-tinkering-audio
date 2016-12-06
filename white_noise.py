import math
import numpy
import pyaudio
import wave
import itertools
import random
import struct
import sys
import winsound
import pygame
from pygame.locals import*

pygame.init()
Clock = pygame.time.Clock()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
window.fill((255, 255, 255))
pygame.display.set_caption('Rubber Biscuits')

SAMPLE_LENGTH = 44100
frames = []
SAMPLE_RATE = 220
SAMPLE_WIDTH = float(44100)
FREQUENCY = 1
VOLUME = 500
BIT_DEPTH = 705
CHANNELS = 1

soundFile = wave.open('sound.wav', 'w')
soundFile.setparams((1, 2, 44100, 44100*8, 'NONE', 'not compressed'))


def puretone():
    for i in range(0, SAMPLE_LENGTH):
        value = math.cos(5.0 * math.pi * FREQUENCY * (i/SAMPLE_RATE) * (VOLUME * BIT_DEPTH))
        packed_value = struct.pack('h', value)
        soundFile.writeframes(packed_value)

def whitenoise():
    for i in range(0, SAMPLE_LENGTH):
        value = math.cos(5.0 * math.pi * FREQUENCY * (i / SAMPLE_RATE) * (VOLUME * BIT_DEPTH))
        packed_value = struct.pack('h', value)
        soundFile.writeframes(packed_value)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_p:
            puretone()
            soundFile.play()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            soundFile.close()
    pygame.display.update()

soundFile.close