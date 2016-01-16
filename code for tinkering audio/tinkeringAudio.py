import random

#function for generating a tone.

def toneGeneration(sec, freq, amplitude):
    buildSin = makeEmptySoundBySeconds(secs)                  #building the clip
    sample_rate = getSamplingRate(buildSin)
    interval = 1.0/freq
    samplesPerCycle = interval * sample_rate                   #working out the samples per cycle.
    maxCycle = 2 * pi
    for pos in range (0,getLength(buildSin)):
        rawSample = sin((pos / samplesPerCycle) * maxCycle)   
        sampleValue = int(amplitude * rawSample)              #gets the value of the sample.
        setSampleValueAt(buildSin, pos, sampleValue)          #sets the value of the tone.
    play(buildSin)
    

#tone combination
def sound():
  file = makeSound(pickAFile())
  play(file)
  
#this function takes the sound files and merges them together. 
def toneCombination():
  s1 = makeSound(pickAFile())                                                            #gets a sound file
  s2 = makeSound(pickAFile())
  canvas = makeEmptySoundBySeconds(5)                                                    #makes a blank sound
  for index in range(0, getLength(s1)):                                                  #gets the length of sound1
    combinationSoundSample1 = getSampleValueAt(s1, index)                                #gets value of sound samples
  for index in range(0, getLength(s2)):
    combinationSoundSample2 = getSampleValueAt(s2, index)
    setSampleValueAt(canvas, index, combinationSoundSample1 + combinationSoundSample2)   #combines the sounds together
  play(canvas)
  return canvas


#audio envelops and echos.

def echoes(delay, num):                                             
  sound = makeSound(pickAFile())
  lengthSound = getLength(sound)                                              #make empty sound
  canvasLengthSound = lengthSound + (delay * num)                                            
  canvas = makeEmptySound(canvasLengthSound)                                  #define sound length
  
  echoAmplitude = 1.0
  for echoCount in range(1, num):                                   
    echoAmplitude = echoAmplitude * 0.5                                      #volume of echo is halfed each time
    for posns in range(0, lengthSound):
      posnsCanvas = posns + ( delay * echoCount)                        
      soundvalue = getSampleValueAt (sound, posns) * echoAmplitude    
      canvasvalues = getSampleValueAt(canvas, posnsCanvas)
      setSampleValueAt(canvas, posnsCanvas, soundvalues + canvasvalues)                    #sets the sample to the canvas
  play(canvas)
  
  
#function for splicing and swapping audio.

def spliceAndSwap():
  s1 = makeSound(pickAFile())                           
  s2 = makeEmptySoundBySeconds(10)                     #This creates a blank canvas
  targetIndex = 1
  for sourceIndex in range (20000, 40000):             #gets the sample values between the ranges
    value = getSampleValueAt(s1, sourceIndex)
    setSampleValueAt(s2, targetIndex, value)           #sets the value to the blank canvas
    targetIndex = targetIndex + 1                      #moves the target index
  for sourceIndex in range (70000, 80000):
    value = getSampleValueAt(s1, sourceIndex)
    setSampleValueAt(s2, targetIndex, value)
    targetIndex = targetIndex + 1
  for index in range(0, 10000):
    setSampleValueAt(s2, targetIndex, 0)               #creates blank sound after
    targetIndex = targetIndex + 1            
  explore(s2)
  return s2


#token parsing

def toneGeneration(frequency):
    buildSin = makeEmptySoundBySeconds(2)                    #building the clip
    amplitude = 2000
    sampleRate = getSamplingRate(buildSin)
    interval = 1.0/frequency
    samplesPerCycle = interval * sampleRate                   #working out the samples per cycle.
    maxCycle = 2 * pi
    for pos in range (0,getLength(buildSin)):
        rawSample = sin((pos / samplesPerCycle) * maxCycle)   
        sampleValue = int(amplitude * rawSample)              #gets the value of the sample.
        setSampleValueAt(buildSin, pos, sampleValue)          #sets the value of the tone.
    play(buildSin)

#selecting frequency to imput to make a sound
def makingSounds():
  frequency = requestNumber ("inputNumber")                   #requests frequency
  toneGeneration(frequency)                                   #inputs frequency to tone generation
  
  
#Random audio generation.
import random

def randomAudio():
  sound = makeEmptySoundBySeconds(5)
  amplitude = random.randrange(1000, 9000)
  for pos in range (getLength(sound)):
        rawSample = random.uniform(-1, 1)   
        sampleValue = int(amplitude * rawSample)              #gets the value of the sample.
        setSampleValueAt(sound, pos, sampleValue)          #sets the value of the tone.
  play(sound)
  explore(sound)