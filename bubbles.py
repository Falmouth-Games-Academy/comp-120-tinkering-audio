import wave, struct, math, cmath, random
import pygame, sys, winsound

sound = wave.open('bubble.wav', 'w')
sound.getparams()
print sound.getparams()

sound2 = wave.open('bubble2.wav', 'w')
sound2.setparams((2, 2, 44100, 44100*10, 'NONE', 'not compressed'))

channels = 2
samplewidth = 2
samplerate = 44100
samplelength = 110250


def echo(bubble, delay):
s1 = sound
s2 = sound
for index in xrange (delay, len(s1)):
    echo = 0.7*110250(s2, index - delay)
    combo = 110250 (s1, index) + echo
    s1[index] = combo
    packaged_value = struct.pack("<h", s1[index])

sound.close()