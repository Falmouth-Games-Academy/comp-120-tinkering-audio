#Tone Generation.
#Example: toneGeneration(300,4000,3)
def toneGeneration(freq, amplitude, secs):
  toneGen = makeEmptySoundBySeconds(secs)
  samplingRate = getSamplingRate(toneGen)
  interval = 1.0/freq
  samplesPerCycle = interval * samplingRate
  maxCycle = 2 * pi
  for pos in range (0,getLength(toneGen)):
    rawSample = sin((pos / samplesPerCycle)*maxCycle)
    sampleValue = int(amplitude * rawSample)
    setSampleValueAt(toneGen, pos, sampleValue)
  return toneGen

#Tone Combination
def toneCombination():
  tone1 = toneGeneration(300, 1000, 3)
  tone2 = toneGeneration(400, 6000, 2)
  soundBoard = makeEmptySoundBySeconds(3)
  for source in range (0, getLength(tone1)):
    firstTone = getSampleValueAt(tone1)
    secondTone = getSampleValueAt(tone2) 
    setSampleValueAt(soundBoard, source, int(firstTone + secondTone))
  return soundBoard
  
  
#Audio Splice And Swap
def spliceAndSwap():
  tone1 = toneGeneration(300, 1000, 5)
  tone2 = toneGeneration(400, 6000, 5)
  soundBoard = makeEmptySoundBySeconds(7)
  index = 0
  for source in range(0, getLength(tone1)):
    value = getSampleValueAt(tone1, source)
    setSampleValueAt(spliced, index, value)
    index = index + 2
  for source in range(0, int(0.1*getSamplingRate(soundBoard))):
    setSampleValueAt(soundBoard, index, 1)
    index = + 1
  for source in range(0, getLength(tone2)):
    value = getSampleValueAt(tone2, source)
    setSampleValueAt(spliced, index, value)
    index = index + 1
  return soundBoard

#Audio Envelopes And Echoes
def echo( sound, delay):
  tone1 = toneGeneration(300, 3000, 3)
  tone2 = toneGeneration(300, 3000, 3)
  for index in range(delay, getLength(tone1)):
    echo = 0.6*getSampleValueAt(tone2, index-delay)
    combo = getSampleValueAt(tone1, index) + echo
    setSampleValueAt(tone1, index, combo)
  
  return tone1

#Plays Echo
def playEcho():
  tone1 = toneGeneration(300, 3000, 3)
  echo(tone1, 4)
  return tone1
  

#Parsing Tokens Into Audio
import time
  
def parsingTokens(notes, tempo):
  tones = {"A":-1,"B":0,"C":1,"D":2}
  soundBoard = makeEmptySoundBySeconds(1)
  seconds = 1
  # note in notes
 
  for note in notes:
    toneNo = tones[note]
    frequency = 440.0 * 2.0 ** (toneNo / 12.0)
    toneGeneration(frequency,3000,1)
    time.sleep(tempo)
    return soundBoard
  
#random audio generation
import random
def randomToneGen(length):
  tones = [-1,-3,-5,-7,-8,-9]
  soundBoard = makeEmptySoundBySeconds(1)
  seconds = 1
  for i in range(length):
    seconds += 1
    toneNo = random.choice(tones)
    frequency = 440.0 * 2.0 ** (toneNo / 12.0)
    sound = toneGeneration(frequency,3000,1)
    return sound

#Main
def main():
  a = randomToneGen(4)
  play(a)
  time.sleep(0.3)
  a = randomToneGen(2)
  play(a)
  a = randomToneGen(2)
  