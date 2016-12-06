import sys
import wave
import math
import struct
import random

soundFile = wave.open('rubber_biscuit.wav', 'w')
rate = 44100

values = []
soundFile.setnchannels(1)
soundFile.setsampwidth(2)
soundFile.setframerate(rate)
SAMPLE_LENGTH = soundFile.getnframes()
FRAMES = []
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
    FREQUENCY = 1
    for i in range(44100):
        value = math.sin(2.0 * math.pi*FREQUENCY*(i/SAMPLE_RATE)) * (VOLUME * BIT_DEPTH)
        packaged_value = struct.pack('<h', value)
        FREQUENCY += -1
        for j in range(0, 1):
            value.append(packaged_value)

def unpackfile():
    wave_packed = soundFile.readframes(1)
    unpack = struct.unpack("<h", wave_packed)
    FRAMES.append(int(unpack[0]))

def writefile():

def echo():
    values = []
    channels = 1
