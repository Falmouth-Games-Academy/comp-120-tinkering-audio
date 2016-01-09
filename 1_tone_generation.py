""" Algorithm One: Tone Generation
This algorithm generates a tone from a sin wave from the users specified frequency, amplitude and length in seconds"""

def toneGen(frequency, amplitude, length):
 makeTone = makeEmptySoundBySeconds(length)
 samplingRate = getSamplingRate(makeTone)
 interval = 1.0 / freq
 samplesPerCycle = interval * samplingRate
 maxCycle = 2 * pi
 for pos in range(getLength(makeTone)):
   rawSample = sin((pos / samplesPerCycle) * maxCycle)
   sampleVal = int(amplitude * rawSample)
   setSampleValueAt(makeTone, pos, sampleVal)
 return makeTone