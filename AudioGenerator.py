import math
import wave
import struct

numChannels = 1
audioHz = 44100

#makes a sine wave
sinWave = []
for index in range(0,90000):
    sinWave.append(math.sin(index))
for sample in sinWave:
    sample = int(sample*32767.0)                                         # 32767.0 is the max amp for 16bit audio
    print sample

struct.pack('h', 1000)

w = wave.open('sound1.wav', 'w')
w.setparams((1, 2, audioHz, len(sinWave), 'NONE', 'not compressed'))

for sample in sinWave:
    data = ''.join(''.join(struct.pack('h', sample*32767)))              # .join allows me to put the list into a string
    w.writeframes(data)
w.close()



#code thus far only exists outside of JES thanks to the work of zach denton who posted a tutorial for a more complicated
#version
#DENTON, Zach. n.d. 'Generate audio with python'. Zach Denton [online].
#Available at: https://zach.se/generate-audio-with-python/ [accessed 11 December 2015].