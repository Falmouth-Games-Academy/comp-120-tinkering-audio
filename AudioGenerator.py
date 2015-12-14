import math
import wave
import struct
import os

numChannels = 1                                                        # Decides whether your in mono or stereo
audioHz = 44100                                                        # Sample rate
maxAmp = 32767                                                         # 32767.0 is the max amp for 16bit audio
amplitude = 1

#makes a list of sin values to be converted later
def makeSin(audioHz, frequency, numSample, maxAmp, amplitude):
    sinWave = []
    sampleRate = audioHz / (numSample / audioHz)
    interval = 1.0/frequency
    samplesPerCycle = interval * sampleRate
    for sample in range(0,numSample):
        rawSample = math.sin(sample / samplesPerCycle)
        sampleValue = rawSample * amplitude
        #These conditions allow you to write the file even if you peak the audio with the amplitude parameter.
        if sampleValue > 1:
            sampleValue = 1
        elif sampleValue < -1:
            sampleValue = -1
        sinWave.append(sampleValue)

    return sinWave

def writeToFile(sinSound, fileName, numChannels, maxAmp):
    struct.pack('h', 1000)
    file = wave.open(str(fileName) + '.wav', 'w')
    file.setparams((numChannels, 2, audioHz, len(sinSound), 'NONE', 'not compressed'))
    for sample in sinSound:                                            # converts sin wave to  16 bit depth audio values
        sample = int(sample*maxAmp)
        data = ''.join(''.join(struct.pack('h', sample)))              # .join allows me to put the list into a string
        file.writeframes(data)
    file.close()
    return str(fileName)

#finds and plays a file in your OS's default media player
def playFile(fileName):
    fileLocation = str(__file__)
    fileLocation = fileLocation.replace('AudioGenerator.py', '', 1)
    fileLocation = fileLocation + str(fileName) + '.wav'
    os.system('start ' + fileLocation)
    return fileLocation

def mergeSin(list1, list2, startPoint):                                # list 1 should be the larger sin list
    for sample in range(startPoint, len(list1)):
        newSample = list1[sample] + list2[sample]
        newSample = newSample / 2
        list1[sample] = newSample
    return list1

print 'generating first sin...'
sin1 = makeSin(audioHz, 440, 3*audioHz, maxAmp, amplitude)
print 'generating second sin...'
sin2 = makeSin(audioHz, 220, 3*audioHz, maxAmp, amplitude)
print 'merging sin waves...'
sin1 = mergeSin(sin1, sin2, 0)
print 'writing file...'
sound = writeToFile(sin1, 'mySound', numChannels, maxAmp)
print 'finding and playing file...'
playFile(sound)