#Algorithm Two: Tone Combination
#This algorithm will combine two tones into one sound file

#Algorithm 1 included to generated tones for combination
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

sampleRate = 44100
def combineTone(tone1, tone2, sampleRate):
  outTone = makeEmptySound(int(sampleRate* seconds), sampleRate)
  for i in range (0, getLength(tone1)):
    firstTone = getSampleValueAt(tone1, i)
    secondTone = getSampleValueAt(tone2, i) 
    setSampleValueAt(outTone, i, int(firstTone + secondTone))
  explore(outTone)
