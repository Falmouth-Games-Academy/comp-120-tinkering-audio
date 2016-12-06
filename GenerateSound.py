import sys
import wave
import math
import struct
import random
import argparse
from itertools import *

values = []
SAMPLE_LENGTH = 44100*8
FREQUENCY = 560
SAMPLE_RATE = float(44100)
VOLUME = 1
BIT_DEPTH = 32767
CHANNELS = 2
timer = 0

def tonegenerator():
    for i in range(0, SAMPLE_LENGTH):
        value = sin(2.0*PI*FREQUENCY*(i/SAMPLE_RATE))*(VOLUME*BIT_DEPTH)

        packaged_value  = package(wav, value)

        for j in xrange(0, CHANNELS):
            values.append(packaged_value)

def increaseVolume():
    for i in range():
        value = getSampleValue(sample)
        setSampleValue(sample, value*2)

def white_noise():


def write_wavefile():

    w = wave.open(filename, 'w')
    w.setparams((CHANNELS, SAMPLE_LENGTH, FREQUENCY, SAMPLE_RATE, 'NONE', 'not compressed'))

    w.write(value_str)
    w.close()

    return filename