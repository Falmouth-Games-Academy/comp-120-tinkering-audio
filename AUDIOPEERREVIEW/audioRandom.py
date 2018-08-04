import wave
import math
import struct
import random

FILE='randomHell.wav'
SAMPLE_LENGTH=13230000
FREQUENCY=2200
SAMPLE_WIDTH=2
SAMPLE_RATE=44100
VOLUME=3000
BIT_DEPTH=16
CHANNELS=2
FORMAT='h'

s_effect=wave.open('randomHell.wav','w')
s_effect.setparams((CHANNELS, SAMPLE_WIDTH, SAMPLE_RATE, 0, 'NONE', 'not compressed'))

values=[]

for i in range(0,SAMPLE_LENGTH):
    value = random.randint(-32767, 32767)
    packed_value = struct.pack('h', value)

    for j in xrange(0,CHANNELS):
        values.append(packed_value)


value_str=''.join(values)
s_effect.writeframes(value_str)
s_effect.close()
