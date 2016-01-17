#Tone Generation.
def tonegen(toneLength, frequency, amplitude):
  s1 = makeEmptySound(toneLength, 44100)
  sampleRate = getSamplingRate(s1)
  Interval = 1.0 / (frequency)
  sampleperc = Interval * sampleRate
  maxCycle = 2 * math.pi
  for sample in range (0, toneLength):
    newSample = math.sin((sample / sampleperc)* maxCycle)
    sampleValue = int (amplitude*newSample)
    setSampleValueAt(s1,sample, sampleValue)
  return s1 
# play (tonegen(44100, 600, 80))
# Amplitude  is in percentage format
# ToneLength is the number of samples in sound
# look online for the values of tones 

def splice():
   file = getMediaPath('AirG.wav')
   source = makeSound(file)
   target = makeSound(file)
   targetIndex =145360 
   for sourceIndex in range(145360, 224755):
     setSampleValueAt(target , targetIndex, getSampleValueAt(source, sourceIndex))
     targetIndex = targetIndex + 1     
   for index in range(0, 1000)
     setSampleValueAt(target, targetIndex, 0)
     targetIndex = targetIndex + 1
   play(target) 
   return target

#Tone Combination
def tonecomb(t1, t2):
  for sample in range(0, getNumSamples(s1)):
    NewSample = getSampleValueAt(t1, sample) + getSampleValueAt(t2, sample)
    setSampleValueAt(t1, sample, NewSample / 2)
  return t1
# play(tonecomb(tonegen(44100, 440, 80), tonegen(44100, 880, 80)))


#Audio Envelopes
def echo( sound, delay):
  t1 = tonegen(300, 3000, 3)
  t2 = tonegen(300, 3000, 3)
  for index in range(delay, getLength(tone1)):
    echo = 0.6*getSampleValueAt(t2, index-delay)
    combo = getSampleValueAt(t1, index) + echo
    setSampleValueAt(t1, index, combo)
  
  return t1

#Plays Echo
def Echo1():
  t1 = tonegen(44100, 600, 80)
  echo(t1, 4)
  return t1
  

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
    tonegen(frequency,3000,1)
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
    sound = tonegen(frequency,3000,1)
    return sound