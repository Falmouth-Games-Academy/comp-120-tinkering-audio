import wave
import math
import struct

samplerate = float(44100) # Hz
SampleLength = 44100 * 4 # seconds
frequency = 440 # Hz
amplitude = 1
samples = frequency*samplerate
BitDepth = 32767

#Tuple of attributes of the wav file
Soundtuple = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
noise_out = wave.open('Alesis-Fusion-Acoustic-Bass-C2.wav','w')
noise_in = wave.open('noise2.wav', 'r')
noise_out.setparams(Soundtuple)

values = []
#unpackaging the wav file so we get understandable values
for i in range(0, Soundtuple[3]):
    value = math.sin(2.0 * math.pi * frequency * (i/Soundtuple[2])) * (amplitude * BitDepth)
    #print value
    packaged_value = struct.unpack('<h', value)

    for j in xrange(0,Soundtuple[0]):
        values.append(packaged_value)

print values


#adds an echo to the wav file through a delay and lowering of volume
#Update, corrupts file and dont know why 0-0
def echo(sndFile, delay):
    values = []
    Channels = 1
    s1 = sndFile
    s2 = sndFile[:]
    for index in range(delay, len(s1)):
        echo = 0.6*s2[index-delay]
        combo = (s1, index) + echo
        s1[index] = combo
        packaged_value = struct.pack("<h", s1[index])
        for j in xrange(Channels):
            values.append(packaged_value)
    value_str = ''.join(values)
    noise_out.writeframes(value_str)
    noise_out.close()
    return values


#increases volume by making the amplitude of the waves bigger
def increase_volume(frames, length):
    for i in xrange(length):
        frames[i] *= 2

echo(noise_in, 8000)