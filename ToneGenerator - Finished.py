import wave
import struct
import math
import random

framevalues = []

def decoder():
    import wave
    import struct

    clip = wave.open('noise2.wav', 'r')
    frames = clip.getnframes()

    for i in range(0, frames):
        soundinfo = clip.readframes(1)
        clipstruct = struct.unpack("<h", soundinfo)
        framevalues.append(int(clipstruct[0]))
        #print(int(clipstruct[0]))


def tonegen():
    noise_out = wave.open('noise2.wav', 'w')

    SAMPLE_RATE = float(44100) # Hz
    SAMPLE_LENGTH = 44100 * 4 # seconds
    FREQUENCY = 440 # Hz
    VOLUME = 1
    BIT_DEPTH = 32767

    Soundtuple = (1, 4, 44100, (44100*4), 'NONE', 'Not compressed')
    noise_out.setparams(Soundtuple)

    values = []

    for i in range(0, SAMPLE_LENGTH):
       value = math.sin(
           2.0 *math.pi *
           FREQUENCY *
            ( i / SAMPLE_RATE)
           )*                  \
            (VOLUME * BIT_DEPTH)
       packaged_value = struct.pack('<h', value)
       for j in xrange(0, 1):
            values.append(packaged_value)

    value_str = ''.join(values)
    noise_out.writeframes(value_str)

    noise_out.close()


def synth():
    samplerate = float(44100)  # Hz
    SampleLength = 44100 * 4  # seconds
    frequency = 440  # Hz
    amplitude = 1
    BitDepth = 32767

    # Tuple of attributes of the wav file
    Soundtuple = (1, 2, samplerate, SampleLength, 'NONE', 'Not compressed')
    noise_out = wave.open('Alesis-Fusion-Acoustic-Bass-C2.wav', 'w')
    noise_out.setparams(Soundtuple)

    values = []
    # unpackaging the wav file so we get understandable values
    for i in range(0, Soundtuple[3]):
        value = math.sin(2.0 * math.pi * frequency * (i / Soundtuple[2])) * (amplitude * BitDepth)
        # print value
        packaged_value = struct.unpack('<h', value)

        for j in xrange(0, Soundtuple[0]):
            values.append(packaged_value)

    print values

#adds an echo to the wav file through a delay and lowering of volume
def echo(sndFile, delay):
    noise_out = wave.open('shutup.wav', 'w')
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

#Creates blank file and adds whitenoise
def whitenoise():
    length = 44100 * 0.5 #seconds
    amplitude = 32767

    #creates blank noise
    noise = wave.open('whitenoise.wav', 'w')
    noise.setparams((1, 2, 44100, length, 'NONE', 'Not compressed'))

    #Generates white noise
    for pos in range(int(length)):
        rawsample = random.uniform(-1, 1)
        samplevalue = int(amplitude * rawsample)
        packedvalue = struct.pack("<h", samplevalue)
        noise.writeframes(packedvalue)
        print '' + str(pos) + ' of ' + str(length) + ': ' + packedvalue
    return noise

echo(framevalues, delay)
