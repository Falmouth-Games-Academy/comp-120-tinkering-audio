#File name: main.py
import time
import random

#Algorithm One: Tone Generation
def tone_generation(frequency, amplitude, length):
  """This algorithm generates a tone from a sine wave from the users specified frequency, amplitude and length in seconds"""
  make_tone = makeEmptySoundBySeconds(length)
  sampling_rate = getSamplingRate(make_tone)
  interval = 1.0 / frequency
  samples_per_cycle = interval * sampling_rate
  max_cycle = 2 * pi
  for pos in range(getLength(make_tone)):
    raw_sample = sin((pos / samples_per_cycle) * max_cycle)
    sample_value = int(amplitude * raw_sample)
    setSampleValueAt(make_tone, pos, sample_value)
  return make_tone

#Algorithm Two: Tone Combination
sample_rate = 44100
def combine_tone(tone1, tone2, sample_rate, seconds):
  """This algorithm combines two tones together."""
  out_tone = makeEmptySound(int(sample_rate* seconds), sample_rate)
  for i in range (0, getLength(tone1)):
    first_tone = getSampleValueAt(tone1, i)
    second_tone = getSampleValueAt(tone2, i) 
    setSampleValueAt(out_tone, i, int(first_tone + second_tone))
  return out_tone
  

#Algorithm Three: Audio Splice and Swap
def audio_splice(tone1, tone2, seconds):
  """This algorithm plays one tone after the other"""
  spliced_length = getLength(tone1) + getLength(tone2)
  spliced = makeEmptySound(spliced_length)
  index = 0
  for source in range(0, getLength(tone1)):
    value = getSampleValueAt(tone1, source)
    setSampleValueAt(spliced, index, value)
    index = index + 1
  for source in range(0, getLength(tone2)):
    value = getSampleValueAt(tone2, source)
    setSampleValueAt(spliced, index, value)
    index = index + 1
  return spliced
 
#Algorithm Four: Echo
"""This function takes a sound and then echoes it by however many seconds specified"""
def echo(delay, sound):
  echo = duplicateSound(sound)
  for index in range(delay, getLength(sound)):
    echo_sample = 0.6*getSampleValueAt(echo, index-delay)
    combined_sample = getSampleValueAt(sound,index) + echo_sample
    setSampleValueAt(sound, index, combined_sample)
  return sound

    
#Algorithm 5: Parsing Tokens into Audio
def note_maker(note_length):
  """This algorithm generates a melody from a list of notes."""
  notes = {'C': -9, 'C#': -8, 'D': -7, 'D#': -6, 'E': -5, 'F':-4, 'F#': -3, 'G': -2, 'G#': -1, 'A': 0, 'A#': 1, 'B': 2, 'c': 3}
  #notes dictionary, each note has an assigned value
  #melody = ['C', 'D' ,'E' ,'G', 'A']
  for n in melody:
    note_number = notes.get(n)
    frequency = 440.0 * 2.0 **(note_number / 12.0)
    tone = tone_generation(frequency, 4000, note_length)    
    play(tone)
    time.sleep(0.95)
    
#Algorithm 6: Random Audio Generation
def random_audio(audio_length, note_length):
  notes = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 5]
  the_tone = makeEmptySoundBySeconds(1)
  seconds = 1
  for n in range(audio_length):
    seconds += 1
    note_number = random.choice(notes)
    frequency = 440.0 * 2.0 **(note_number / 12.0)
    tone = tone_generation(frequency, 4000, note_length)    
    combine = audio_splice(the_tone, tone, seconds)
    the_tone = combine
  return combine
  
def export_audio(audio):
  """This function exports the audio as a .wav file so it can be used as gameplay audio"""
  path = setMediaPath()
  writeSoundTo(audio, 'tone.wav')
  



