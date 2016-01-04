#Algorithm One: Tone Generation
#This algorithm generates a tone from a sin wave from the users specified frequency, amplitude and length in seconds.
def toneGen(freq, amplitude, length):
 makeTone = makeEmptySoundBySeconds(length)
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
  
  
#Algorithm Three: Audio Splice and Swap
#This algorithm plays one tone after the other
def audioSplice(tone1, tone2, seconds):
 spliced = makeEmptySound(seconds * 22050)
 index = 0
 for source in range(0, getLength(tone1)):
   value = getSampleValueAt(tone1, source)
   setSampleValueAt(spliced, index, value)
   index = index + 1
 for source in range(0, int(0.1*getSamplingRate(spliced))):
   setSampleValueAt(spliced, index, 0)
   index = index + 1
 for source in range(0, getLength(tone2)):
   value = getSampleValueAt(tone2, source)
   setSampleValueAt(spliced, index, value)
   index = index + 1
 play(spliced)
 return spliced
 
 
#Algorithm ThreeB: Audio Splice and Swap
#This algorithm splices one tone into another

#Algorithm Four A: Envelope 

#Algorithm Four B: Echo
def echo(sound1, sound2, second_delay):
  for i in range(second_delay, getLength(sound1)):
    echo = 0.6*getSampleValueAt(sound2, i-second_delay)
    combo = getSampleValueAt(sound1, i) + echo
    setSampleValueAt(sound1, i, combo)
  play(sound1)
  return sound1



 

