import math
import wave
import struct
import os
import random

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

def makeNoise (numSample, maxAmp):
    noiseList = []
    for index in range(0, numSample):
        sample = random.randint(maxAmp * -1, maxAmp) / float(maxAmp)
        noiseList.append(sample)
    return noiseList

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
    fileLocation = fileLocation.replace('AudioGenerator.py', str(fileName) + '.wav', 1)
    os.system('start ' + fileLocation)
    return fileLocation

def mergeSound(list1, list2, startPoint):                              # list 1 should be the larger sin list
    for sample in range(startPoint, len(list1)):                       # currently has a bug where you must merge
        if sample < len(list2):                                        #  with a sin wave for the code to work
            newSample = list1[sample] + list2[sample]
            newSample = newSample / 2.0
            list1[sample] = newSample
        else:
            break
    return list1

def loadFile(fileName):                                                # Must be mono and have a 16 bit depth
    file = wave.open(fileName + '.wav', 'r')
    sampleList = []
    numSamples = file.getnframes()
    for sample in range(0, numSamples):
        rawData = file.readframes(1)
        data = struct.unpack('<h', rawData)
        sampleList.append(data[0]/32767.0)
    return sampleList

def stringSound(sound1,sound2):                                        # strings one sound onto the end of another
    for sample in range(0, len(sound2)):
        sound1.append(sound2[sample])
    return sound1

def echoSound(soundList, numEcho, sampleGap, volumeDecrease):
    for echo in range(1, numEcho + 1):
        sampleDifference = (echo + 1) * sampleGap
        for sample in range(sampleDifference, len(soundList)):
                newSample = soundList[sample] + soundList[sample - sampleDifference]
                volumeChange = volumeDecrease * echo
                if volumeChange <= 1 and volumeChange >= 0:
                    newSample = (newSample * volumeChange) / 2
                    soundList[sample] = newSample
    return soundList

#sound = loadFile(sound3)
#sound = echoSound(sound, 60, 1000)
#writeToFile(sound,)




#test code
print "Loading files..."
clock = loadFile('testClock')
print 'Making sounds...'
sin1 = makeSin(audioHz, 220, 3*audioHz, maxAmp, amplitude)
sin2 = makeSin(audioHz, 440, 3*audioHz, maxAmp, amplitude)
noise = makeNoise(3*audioHz, maxAmp)
print 'Merging...'
clock = mergeSound(clock, sin1, 1*audioHz)
clock = mergeSound(clock, sin2, 2*audioHz)
clock = stringSound(clock, noise)
print 'Adding echo...'
clock = echoSound(clock, 10, audioHz, 0.8)
print 'Saving '+str(len(clock))+' samples...'
print 'This may take a while'
writeToFile(clock, 'testOutput', numChannels, maxAmp)
print 'Playing...'
playFile('testOutput')
