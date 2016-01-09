"""Tone gernation algorithm to generate tones that will then be combine"""
def importSound():
  file = pickAFile()
  sound = makeSound(file)
  play(sound)
  return sound

#Algorithm 1 included to generate tones
def toneGen(freq, amplitude, length):
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


#Algorithm Three: Audio Splice and Swap
#This algorithm plays one tone after the other

def audioSplice(tone1, tone2, seconds):
 spliced_length = int(getLength(tone1) + getLength(tone2))
 spliced = makeEmptySound(spliced_length)
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
 
 #Audio Splice And Swap
def spliceAndSwap():
  tone1 = toneGen(300, 1000, 5)
  tone2 = toneGen(400, 6000, 5)
  soundBoard = makeEmptySoundBySeconds(7)
  index = 0
  for source in range(0, getLength(tone1)):
    value = getSampleValueAt(tone1, source)
    setSampleValueAt(soundBoard, index, value)
    index = index + 2
  for source in range(0, int(0.1*getSamplingRate(soundBoard))):
    setSampleValueAt(soundBoard, index, 1)
    index = + 1
  for source in range(0, getLength(tone2)):
    value = getSampleValueAt(tone2, source)
    setSampleValueAt(soundBoard, index, value)
    index = index + 1
  play(soundBoard)