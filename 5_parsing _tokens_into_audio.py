import time

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
 play(makeTone)
 return makeTone
 
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

  
  
  

