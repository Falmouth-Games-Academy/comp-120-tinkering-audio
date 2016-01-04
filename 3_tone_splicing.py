"""Tone gernation algorithm to generate tones that will then be combine"""
def importSound():
  file = pickAFile()
  sound = makeSound(file)
  play(sound)
  return sound


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