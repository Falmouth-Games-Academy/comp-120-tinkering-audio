import wave
import struct
import math

amplitude = 0.4
BitDepth = 65000

Sound = wave.open('mellow.wav','r')
Soundtuple = Sound.getparams()

for i in range(0, Soundtuple[3]):
    Soundinfo = Sound.readframes(1)
    Soundstruct = struct.unpack("<h",Soundinfo)

Soundtuple = Sound.getparams()

Sound2 = wave.open('mellow2.wav','r')
Soundtuple2 = Sound2.getparams()

for x in range(0, Soundtuple2[3]):
    Sound2info = Sound2.readframes(1)
    Sound2struct = struct.unpack("<h", Sound2info)

noise_out_tuple = (1, 2, 44100, 176400,'NONE', 'Not compressed')
noise_out = wave.open('Melody.wav', 'w')
noise_out.setparams(noise_out_tuple)

values = []
for y in range(0, noise_out_tuple[3]):
    value = math.sin(2.0 * math.pi * (y / noise_out_tuple[2])) * (amplitude * BitDepth)
    print value
    packaged_value = struct.pack('h', value)

    for j in xrange(0, noise_out_tuple[0]):
        values.append(packaged_value)

print Soundtuple
print Soundtuple2
noise_out.writeframes(str(values))
noise_out.close()
