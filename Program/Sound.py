__author__='James'

import random
import time


# Algorithm 1: Generating Sound
'''From introduction to Python page 267'''
def sine_Wave(frequency, amplitude, length): 
  # Create a blank sound 
  build_Sin = makeEmptySoundBySeconds(length)
  # Set constants 
  samplingRate = getSamplingRate(build_Sin) 
  interval = 1.0 / frequency
  samplesPerCycle = interval * samplingRate 
  maxCycle = 2 * pi 
  # Generate the sound 
  for pos in range(getLength(build_Sin)): 
    rawSample = sin((pos / samplesPerCycle) * maxCycle) 
    sampleVal = int(amplitude * rawSample) 
    setSampleValueAt(build_Sin, pos, sampleVal)
  return build_Sin
  

# Algorithm 2: Merging two sounds together
'''From introduction to Python page 267''' 
def merge(sound_1, sound_2):
  for sample in range(0, getLength(sound_1)): 
    sample_1 = getSampleValueAt(sound_1, sample)
    sample_2 = getSampleValueAt(sound_2, sample)
    setSampleValueAt(sound_1, sample, int(sample_1 + sample_2))
    merged_Sound = sound_1
  return merged_Sound
  

# Algorithm 3: Splicing
'''From introduction to Python page 244'''
def splice(tone_1):
  '''tone_1 is played first followd by the tone_2 then tone_1'''
  tone_2 = makeEmptySoundBySeconds(5)
  targetIndex = 17408
  for sourceIndex in range(33414, 40052):
    value = getSampleValueAt(tone_2, sourceIndex)
    setSampleValueAt(tone_1, targetIndex, value)
    targetIndex = targetIndex + 1
  return tone_1
  

# Algorithm 4: Echo
'''From introduction to Python page 260'''
def echo(pre_echo, delay, runs):
  '''pre-echo stands for the original input sound'''
  # Create a new sound, that echoes the input soundfile
  # to the number of runs, each delay apart                                               
  end_1 = getLength(pre_echo)  
  end_2 = end_1 + (delay * runs)                                              
  echo_applied = makeEmptySound(end_2) 
    
  echoAmplitude = 1.0  
  for echoCount in range(1, runs): 
    # The sound is reduced by 60% with each run                                    
    echoAmplitude = echoAmplitude * 0.6 
    for pos_1 in range(0, end_1):  
      pos_2 = pos_1 + ( delay * echoCount)                          
      value_1 = getSampleValueAt (pre_echo, pos_1) * echoAmplitude      
      value_2 = getSampleValueAt (echo_applied, pos_2)  
      setSampleValueAt(echo_applied, pos_2, value_1 + value_2)
  return echo_applied

  
# Algorithm 5: Parsing tokens into audio
def melody(note_Length):  
  '''there are two different melodys that can be used, also it uses a reandom frequency to produce interesting results'''
  notes = {'A': -12, 'A#': -11, 'B': -10, 'C': -9, 'C#': -8, 'D': -7, 'D#': -6, 'E': -5, 'F':-4, 'F#': -3, 'G': -2, 'G#': -1, 'a': 0, 'a#': 1, 'b': 2, 'c': 3}  
  # notes dictionary, each note has an assigned value  
  melody_notes = ['F', 'G' ,'F' ,'G', 'E', 'C', 'B', 'D', 'F', 'G' ,'F' ,'G', 'E',]
  # melody_notes = ['D', 'D' ,'C#' ,'D', 'C#', 'D', 'E', 'E', 'G', 'G' ,'F#' ,'D', 'E', 'C#', 'A', 'F#' ,'D', 'E', 'C#', 'A']  
  for n in melody_notes:  
    note = notes.get(n)  
    frequency = 440.0 * 2.0 **(note / 12.0)  
    final_Melody = sine_Wave(frequency, 3000, note_Length)
    echo(final_Melody, 5000, 4)
  return 

# Algorithm 6: Random Audio Generation  
def random_Notes(note_Length): 
  '''This will produce either a random piano note or a random tone'''
  intensity = 64
  dur = 1000
  # r_tone = playNote(random.randrange(40, 80), dur, intensity)
  r_tone = sine_Wave(random.randrange(200, 800), 3000, note_Length)
  sequence = splice(r_tone)
  return sequence
  

'''The main function to write the sounds to file'''  
def main():
  setMediaPath()
  final_song_1 = echo(melody(1), 5000, 4)
  final_song_2 = random_Notes(5)
  writeSoundTo(final_song_1, "Final_Song_1")
  writeSoundTo(final_song_2, "Final_Song_2")