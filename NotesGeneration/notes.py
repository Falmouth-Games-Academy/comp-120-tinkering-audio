import wave, struct, math, random
from noteFrequencies import *


sampleLength = 44100/16
sampleRate = float(44100)
volume = 1
bitDepth = 32767
notePrefix = ['C', 'CS', 'D', 'DS', 'E', 'F', 'FS', 'G', 'GS', 'A', 'AS', 'B']
fSharpMinor = ['FS', 'GS', 'A', 'B', 'CS', 'D', 'E']
CMajor = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


def notegen():
    prefixChoice = random.randint(0, 11)
    suffixChoice = random.randint(0, 1)

    return notePrefix[prefixChoice] + str(4)

soundparams = (2, 2, sampleRate, sampleLength*random.randint(2, 5), 'NONE', 'Not compressed')
soundparams2 = (2, 2, sampleRate, sampleLength*random.randint(2, 5), 'NONE', 'Not compressed')

noise_out = wave.open('melody1.wav', 'w')
noise_out2 = wave.open('melody2.wav', 'w')
cool_noise_out = wave.open('CoolPlaneSound.wav', 'w')

noise_out.setparams(soundparams)
noise_out2.setparams(soundparams2)
cool_noise_out.setparams(soundparams)

values = []
values2 = []
cool_values = []

def savesound(noise):
    noise.close()


def randomnote(identifier, noise):
    noteChoice = notegen()
    for i in range(0, soundparams[3]):
        value = math.sin(2.0 * math.pi * notes[noteChoice] * (i / soundparams[2])) * (volume * bitDepth)
        packaged_value = struct.pack('h', value)

        for j in xrange(0, soundparams[0]):
            identifier.append(packaged_value)
    value_str = ''.join(identifier)
    noise.writeframes(value_str)


def cool_plane_sound():
    loopcount = 0
    melody1 = enumerate(values)
    for index, val in melody1:
        if loopcount < 1000:
            loopcount += 1
            unpacked_values = struct.unpack('h', val)
            unpacked_ints = reduce(lambda rst, d: rst * 10 + d, (unpacked_values))
            packaged_value = struct.pack('h', unpacked_ints)
            for j in xrange(0, soundparams[0]):
                cool_values.append(packaged_value)
            value_str = ''.join(cool_values)
            cool_noise_out.writeframes(value_str)


class Note:
    def __init__(self, (name, frequency), samplerate, samplelength, bitdepth, volume, identifyer):
        #self.frequency = frequency
        self.note = wave.open('Notes/' + str(name) + '_' + identifyer + '.wav', 'w')
        self.note.setparams((2, 2, bitdepth, samplelength, 'NONE', 'not compressed'))
        volume = 0
        length = samplelength

        for i in range(0, samplelength):
            half = (samplelength + 1)/2
            if i < half and volume < 0.9:
                volume = float(i*2)/samplelength
            elif i > half and volume > 0.1:
                volume = samplelength/float(i*2)
            value = math.sin(2.0 * math.pi * frequency * (i / samplerate)) * (volume * bitdepth)
            packed_value = struct.pack('h', value)
            self.note.writeframes(packed_value)
            self.note.writeframes(packed_value)

        self.note.close()



