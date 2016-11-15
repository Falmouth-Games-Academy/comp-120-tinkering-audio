import wave, struct

noise = wave.open('noise2.wav', 'r')
length = noise.getnframes()
framerate = noise.getframerate()
halfwave = 0
waveStart = 0
frames = []

for i in xrange(0, length):
    noiseFrames = noise.readframes(1)
    frameValue = struct.unpack("<h", noiseFrames)
    frames.append(int(frameValue[0]))
    if halfwave < 2:
        if frames[i] == 0:
            if halfwave == 1:
                frequency = framerate / (i - waveStart) / 2
                print "The frequency is " + str(frequency) + "/s"
            else:
                waveStart = i
            halfwave += 1