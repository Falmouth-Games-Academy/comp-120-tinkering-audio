import pygame
import math
import numpy
import random

pygame.init()
pygame.display.set_mode((800, 640))
pygame.mixer.init()

##Variables
samplew = 2
samplerate = 44100.0
bitdepth = 2.0
channels = 2


def generate_tone():
    generate_samples = numpy.array([[1, 1], [2, 2], [3, 3]], dtype="int8") ##generate short tone
    return generate_samples

samples=generate_tone()
current_sound=pygame.sndarray.make_sound(samples)


done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                current_sound.play(-1)

    pygame.display.update()

pygame.mixer.quit()
pygame.quit()