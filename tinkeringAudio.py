#Algorithm One: Tone Generation
#This algorithm generates a tone from a sin wave from the users specifed frequency, amplitude and length in seconds.
def toneGen(freq, amplitude, length):
 # Create a blank sound
 makeTone = makeEmptySoundBySeconds(length)
 # Set constants
 samplingRate = getSamplingRate(makeTone)
 interval = 1.0 / freq
 samplesPerCycle = interval * samplingRate
 maxCycle = 2 * pi
 # Generate the sound
 for pos in range(getLength(makeTone)):
   rawSample = sin((pos / samplesPerCycle) * maxCycle)
   sampleVal = int(amplitude * rawSample)
   setSampleValueAt(makeTone, pos, sampleVal)
 return makeTone
 
#Algorithm Two: Tone Combination
#This algorithm will combine two tones
sampleRate = 44100
def combineTone(tone1, tone2, sampleRate):
  outTone = makeEmptySound(int(sampleRate* seconds), sampleRate)
  for i in range (0, getLength(tone1)):
    firstTone = getSampleValueAt(tone1, i)
    secondTone = getSampleValueAt(tone2, i) 
    setSampleValueAt(outTone, i, int(firstTone + secondTone))
  explore(outTone)
  
#Algorithm TwoB: Tone Combination
#This algorithm will combine three tones
sampleRate = 44100
def combineTone2(tone1, tone2, tone3, sampleRate):
  outTone = makeEmptySound(int(sampleRate* seconds), sampleRate)
  for i in range (0, getLength(tone1)):
    firstTone = getSampleValueAt(tone1, i)
    secondTone = getSampleValueAt(tone2, i) 
    thirdTone = getSampleValueAt(tone3, i) 
    setSampleValueAt(outTone, i, int(firstTone + secondTone + thirdTone))
  explore(outTone)
