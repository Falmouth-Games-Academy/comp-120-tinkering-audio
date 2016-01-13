#File name: main.py

#Algorithm One: Tone Generation
def tone_generation(frequency, amplitude, length):
#This algorithm generates a tone from a sine wave from the users specified frequency, amplitude and length in seconds
 makeTone = makeEmptySoundBySeconds(length)
 samplingRate = getSamplingRate(makeTone)
 interval = 1.0 / frequency
 samplesPerCycle = interval * samplingRate
 maxCycle = 2 * pi
 for pos in range(getLength(makeTone)):
   rawSample = sin((pos / samplesPerCycle) * maxCycle)
   sampleVal = int(amplitude * rawSample)
   setSampleValueAt(makeTone, pos, sampleVal)
 return makeTone

#Algorithm Two: Tone Combination
sampleRate = 44100
def combineTone(tone1, tone2, sampleRate, seconds):
#This algorithm combines two tones together.
  outTone = makeEmptySound(int(sampleRate* seconds), sampleRate)
  for i in range (0, getLength(tone1)):
    firstTone = getSampleValueAt(tone1, i)
    secondTone = getSampleValueAt(tone2, i) 
    setSampleValueAt(outTone, i, int(firstTone + secondTone))
  explore(outTone)
  
#a3
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
 
 #A4
 """This function takes a sound and then echoes it by however many seconds specified"""
def echo(sound1, sound2, second_delay):
  #echo_length = getLength(sound1) + (second_delay* getSamplingRate(sound1)
  for i in range(int(second_delay), getLength(sound1)):
    echo = 0.4*getSampleValueAt(sound2, i-int(second_delay))
    combo = getSampleValueAt(sound1, i) + echo
    setSampleValueAt(sound1, i, combo)
  play(sound1)
  return sound1
  
#Algorithm 5: parsing tokens into audio
#Haven't added tone duration yet
def noteMaker():
  #notes dictionary
  notes = {'C': -9, 'C#': -8, 'D': -7, 'D#': -6, 'E': -5, 'F':-4, 'F#': -3, 'G': -2, 'G#': -1, 'A': 0, 'A#': 1, 'B': 2, 'c': 3}
  
  melody = ['D', 'E' ,'C' ,'D#', 'C']
     
  for n in melody:
    note_number = notes.get(n)
    frequency = 440.0 * 2.0 **(note_number / 12.0)
    tone = toneGen(frequency, 2000, 1)    
    play(tone)
    time.sleep(0.95)
    
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



