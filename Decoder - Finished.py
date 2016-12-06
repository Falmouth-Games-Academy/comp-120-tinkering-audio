import wave
import struct

clip = wave.open('noise2.wav','r')
frames = clip.getnframes()

for i in range(0, frames):
   soundinfo = clip.readframes(1)
   clipstruct = struct.unpack("<h", soundinfo)
   print(int(clipstruct[0]))