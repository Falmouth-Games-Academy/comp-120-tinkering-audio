import math, wave, struct, os, random


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

class Melody:
    def __init__(self, source, volume, defaultPeakLocation, maxAmplitude, hertz):
        self.__source = source
        self.__peak = defaultPeakLocation                              # sets where the peak in each note of the song is
        self.__volume = volume
        self.__maxAmplitude = maxAmplitude
        self.__hertz = hertz

    #makes a list of sin values to be converted later
    def makeSin(self, noteFrequency, numSample):
        sinWave = []
        sampleRate = self.__hertz / (numSample / self.__hertz)
        interval = 1.0/noteFrequency
        samplesPerCycle = interval * sampleRate
        for sample in range(0, numSample):
            rawSample = math.sin(sample / samplesPerCycle)
            sampleValue = rawSample * self.__volume
            #These conditions allow you to write the file even if you peak the audio with the amplitude parameter.
            if sampleValue > 1:
                sampleValue = 1
            elif sampleValue < -1:
                sampleValue = -1
            sinWave.append(sampleValue)
        return sinWave

    def peakSin(self, sin, peakLocation):
        if peakLocation is False:                                      # to use default peak, peakLocation = false
            peakLocation = self.__peak
        peakSample = len(sin) * peakLocation
        for sample in range(0, len(sin)):
            if sample < peakSample:
                factor = 1 / peakSample
                multiplyer = sample * factor
                if multiplyer <= 1:
                    sin[sample] = sin[sample] * multiplyer
            elif sample > peakSample:
                factor = 1 / (len(sin) - peakSample)
                multiplyer = (len(sin) - sample) * factor
                if multiplyer <= 1:
                    sin[sample] = sin[sample] * multiplyer
        return sin

    def stringSound(self, sound1,sound2):                              # strings one sound onto the end of another
        for sample in range(0, len(sound2)):
            sound1.append(sound2[sample])
        return sound1

    #reads a custom format and writes it to a .wav file
    def readMelToSin(self, filename):
        frequencyLib = [('-A', 440), ('A#', 466), ('B', 494), ('C', 523), ('C#', 554), ('D', 587),
                         ('D#', 622), ('E', 659), ('F', 698), ('F#', 739), ('G', 783), ('G#', 830), ('A', 880)]
        if type(self.__source) == str:
            filename = str(filename)+'.mel'                                # mel stands for melody
            file = open(filename, 'r')
            fileList = []
            for line in file:
                line = line.replace('\n', '')
                fileList.append(line)
            for index in range(0, len(fileList)):
                fileList[index] = fileList[index].split(',', 1)
                fileList[index][0] = fileList[index][0].upper()
                fileList[index][1] = int(fileList[index][1])
            self.__source = fileList
        for note in range(0, len(fileList)):
            fileList[note][1] = fileList[note][1] * self.__hertz
            for libNote in range(0, len(frequencyLib)):
                if fileList[note][0] == frequencyLib[libNote][0]:
                    fileList[note][0] = frequencyLib[libNote][1]
        sin = []
        for note in range(0, len(fileList)):
            rawSin = self.makeSin(fileList[note][0], fileList[note][1])
            rawSin = self.peakSin(rawSin, self.__peak)
            sin = self.stringSound(sin, rawSin)
        return sin



#test code
print 'loading clock...'
clock = loadFile('testClock')
print 'generating buffer noise...'
white = makeNoise(audioHz, 32767)
print 'reading melody...'
sound = Melody('BadSong', 1, 0.1, 32767, 44100)
sound = sound.readMelToSin('BadSong')
print 'stringing sounds...'
sound = stringSound(clock, sound)
sound = stringSound(sound, white)
print 'adding echo...'
echoSound(sound, 20, int(0.5*audioHz), 0.9)
print 'writing...'
print 'this often takes a long time'
writeToFile(sound, 'TerribleSong', 1, 32767)
print 'hopefully playing...'
playFile('TerribleSong')
