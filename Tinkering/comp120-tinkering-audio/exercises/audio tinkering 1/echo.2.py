
import wave
import math
import struct

sound1 =""
sound2 =""

SAMPLE_WIDTH=2
SAMPLE_RATE=44100.0
BIT_DEPTH=2.0
CHANNELS=2

#pygame.init()

toneOut = wave.open("PureTone.wav", "w")
toneOut.setparams((2,2,44100,44100,"NONE",""))

values=[]
for i in xrange(0,44100):
    value = math.sin(2.0*3.141*417*i/44100)*32000
    packed = struct.pack("<h",value)
    values.append(packed)

toneOut.writeframes("".join(values))
toneOut.close()


def echo(sound1,sound2,delay,sample_length):
    values=[]
    for i in range(0,sample_length):
        values.append(sound1[i])
        if i>delay:
            echo=sound1[i]*0.6
            values.append(echo+sound1[i])
    return values