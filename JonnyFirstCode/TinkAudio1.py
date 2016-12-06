import wave, struct

Noise = wave.open('noise2.wav')
frames = Noise.getnframes()
samplewidth = Noise.getsampwidth()
framerate = Noise.getframerate()
everything = Noise.getparams()

n = 0
for i in xrange(0, frames):
    NoiseData = Noise.readframes(1)
    NoiseStruct = struct.unpack("<h", NoiseData)
    wave = (int(NoiseStruct[0]))
    print wave
    n += 1

print "No. of frames = ", frames
print "Sample Width = ", samplewidth
print "Frame Rate = ", framerate
print n
print everything

MaxValue = 1683
MaxPossible = 32768

print "max value = 16383"
