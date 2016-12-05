import wave
import math
import struct
import pygame
import sys
from pygame.locals import *

samplerate = float(44100)                                                                                   # Hz
SampleLength = 22050                                                                                        # seconds
amplitude = 0.4
BitDepth = 65000
Soundtuple = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
noise_out = wave.open('keyboard.wav', 'w')
noise_out.setparams(Soundtuple)

values = []


def sound_generator(frequency):
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * frequency * (i/Soundtuple[2])) * (amplitude * BitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)


def whitespace():
    for i in range(0, Soundtuple[3]):
        value = math.sin(0)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)
    value_str = ''.join(values)
    noise_out.writeframes(value_str)


def close_sound():
    noise_out.close()


pygame.init()

Width = 800
Height = 600

window = pygame.display.set_mode((Width, Height), 0, 32)

pygame.display.set_caption('Sound Generation Keyboard')
Black = (0, 0, 0)
White = (255, 255, 255)
font = pygame.font.SysFont(None, 96)


while True:
    window.fill(Black)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if keys[K_a]:
            print 'A4'
            sound_generator(440.000)
        if keys[K_s]:
            print 'E4'
            sound_generator(493.883)

        if keys[K_d]:
            print 'C5'
            sound_generator(523.251)

        if keys[K_f]:
            print 'D5'
            sound_generator(587.330)

        if keys[K_g]:
            print 'E5'
            sound_generator(659.255)

        if keys[K_h]:
            print 'F5'
            sound_generator(698.456)

        if keys[K_j]:
            print 'G5'
            sound_generator(783.991)

        if keys[K_k]:
            print 'A5'
            sound_generator(880.000)

        if keys[K_l]:
            print 'B5'
            sound_generator(987.767)

        if keys[K_z]:
            print 'C6'
            sound_generator(1046.50)

        if keys[K_x]:
            print 'D6'
            sound_generator(1174.66)

        if keys[K_c]:
            print 'E6'
            sound_generator(1318.51)

        if keys[K_v]:
            print 'F6'
            sound_generator(1396.91)

        if keys[K_b]:
            print 'G6'
            sound_generator(1567.98)

        if keys[K_SPACE]:
            print 'Silence'
            whitespace()

        if keys[K_RETURN]:
            print 'Sound Closed'
            close_sound()
			