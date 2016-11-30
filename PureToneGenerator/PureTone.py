from wave import *
import struct
import math

values = []
SAMPLE_LENGTH = 44100*8
FREQUENCY = 290
SAMPLE_RATE = float(44100)
VOLUME = 1
BIT_DEPTH = 32767
CHANNELS = 2
timer = 0
noise_out = open("unknownNoise.wav", "w")
noise_out.setparams((2, 2, 44100, 44100*8, 'NONE', 'not compressed'))

for i in range(0, SAMPLE_LENGTH):
    value = math.sin(2.0 * math.pi*FREQUENCY*( i / SAMPLE_RATE)) * (VOLUME * BIT_DEPTH)
    packaged_value = struct.pack('h', value)

    noise_out.writeframes(packaged_value)
    noise_out.writeframes(packaged_value)
#for j in xrange(0, CHANNELS):
#    values.append (packaged_value)
#    value_str = ''.join(values)
#    noise_out.write (value_str)
noise_out.close()