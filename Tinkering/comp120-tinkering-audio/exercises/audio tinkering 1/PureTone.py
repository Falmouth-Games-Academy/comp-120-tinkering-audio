import pygame
import wave
import struct
import math

pygame.init()



def generate_soundwave(sample_length, frequency, volume):
    values=[]
    for i in xrange(0,sample_length):
        value = math.sin(2.0*3.141*frequency*i/sample_length)*volume
        packed = struct.pack("<h",value)
        values.append(packed)

    return values

def savewav_file(filename, sample_length, values):
    toneOut = wave.open(filename, "w")
    toneOut.setparams((2,2,sample_length,44100,"NONE",""))
    toneOut.writeframes("".join(values))
    toneOut.close()


tone1 = generate_soundwave(44100,417,3200)
pulsarTone = generate_soundwave(44100,450,3200)

savewav_file("tone1.wav", 44100, tone1)
savewav_file("pulsarTone.wav", 44100, pulsarTone)