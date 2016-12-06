import wave, struct, math, cmath, random
import pygame, sys, winsound

sound = wave.open('sound.wav', 'w')
sound.setparams((2, 2, 44100, 44100*10, 'NONE', 'not compressed'))

length = 44100*5
sample_rate = float(44100)
volume = 1
bit_depth = 32767

#eel eletric shock
for i in range(0, length):
    frequency = i/300
    value = math.cos(8.0 * math.pi * frequency * ( i / sample_rate)) * (volume * bit_depth)
    packed_value = struct.pack('h', value)
    sound.writeframes(packed_value)

sound.close()
