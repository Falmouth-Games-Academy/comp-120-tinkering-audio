#Tone Generation Algorithm
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
 play(makeTone)
 return makeTone
 

def noteMaker():
  #notes dictionary
  notes = {'C': -9, 'C#': -8, 'D': -7, 'D#': -6, 'E': -5, 'F':-4, 'F#': -3, 'G': -2, 'G#': -1, 'A': 0, 'A#': 1, 'B': 2, 'c': 3}
  #note, note_length = melody.spilt(':')

  melody = ['D', 'E' ,'C' ,'D']
  
  #frequency = 440.0 * 2.0 **(notess / 12.0)
  #print frequency
  #print frequency
  #tone = toneGen(frequency, 2000, 2)
  
  for key in notes.iterkeys():
    print key
    
  for value in notes.itervalues():
    print value
  

