import time
import random

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
 
def audioSplice(tone1, tone2, seconds):
 spliced_length = (int(getLength(tone1) + getLength(tone2)) + 100)
 spliced = makeEmptySound(spliced_length)
 index = 0
 for source in range(0, getLength(tone1)):
   value = getSampleValueAt(tone1, source)
   setSampleValueAt(spliced, index, value)
   index += 1
# for source in range(0, int(0.1*getSamplingRate(spliced))):
#   setSampleValueAt(spliced, index, 0)
 #  index = index + 1
 for source in range(0, int(0.1 * 44100)):
   setSampleValueAt(spliced, index, 0)
   index += 1
 for source in range(0, getLength(tone2)):
   value = getSampleValueAt(tone2, source)
   setSampleValueAt(spliced, index, value)
   index += 1
 play(spliced)
 return spliced
 

#Algorithm 6: Random Audio Generation
def randomAudio(length):
  notes = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 5]
  aTone = makeEmptySoundBySeconds(1)
  seconds = 1
  for n in range(length):
    seconds += 1
    print seconds
    note_number = random.choice(notes)
    frequency = 440.0 * 2.0 **(note_number / 12.0)
    tone = toneGen(frequency, 2000, 1)    
    combine = audioSplice(aTone, tone, seconds)
    aTone = combine
  play(combine)
  #writeSoundTo(tone, r'G:\Documents\GitHub\COMP120\comp-120-tinkering-audio\n.wav')
