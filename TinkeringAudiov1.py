import pygame
import math
import numpy
import random

# This section intialises pygame and sets the resolution of the monitor used
pygame.init()
pygame.display.set_mode((800, 640))
pygame.mixer.init()

# This section defines the variables that are used
samplew = 2
samplerate = 44100.0
bitdepth = 2.0
chan = 2
volume = 40
sample_length = 2

# This sets definitions in order to calculate and figure out tones
def generate_tone():
    generate_samples = numpy.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], dtype="int8") ##generate short tone
    return generate_samples

def generate_sine_wave(frequency, samplerate, sample_length, volume):
    values = []
    for i in range(0, sample_length):
        value = math.sin(2 * math.pi * frequency * (i / samplerate)) * (volume * bitdepth)

        for j in xrange(0, chan):
            values.append(value)

    return values

def make_chord(sound1,sound2,sound3,sample_length):
    values=[]
    for i in range(0,sample_length):
        values.append(sound1[i])
        if i>4000:
            values.append(sound1[i]+sound2[i])
        if i>8000:
            values.append(sound1[i]+sound2[i]+sound3[i])
    return values

samples=generate_tone()
current_a=pygame.sndarray.make_sound(samples)

# This exits the aapplicaiyon upon pressing the exit button and on pressing a key plays the tone
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_o:
                current_a.play(-1)

    pygame.display.update()

# This generates a sine wave and a sound and then exits the application
tone_values_one=generate_sine_wave(4000.0,samplerate,132000,1000.0)
chord_values=make_chord(generate_tone, 132000)
pygame.mixer.quit()
pygame.quit()