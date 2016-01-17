# File name: main.py
# Author: 1507866

import time
import random

# Algorithm One: Tone Generation
def tone_generation(frequency, amplitude, length):
  """ This algorithm generates a tone from a sine wave from the users specified frequency, amplitude and length in seconds.
  :param frequency:
  :param amplitude:
  :param length:
  :return:
  """
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

# Algorithm Two: Tone Combination
sample_rate = 44100
def combine_tone(tone1, tone2):
  """ This algorithm combines two tones together.
  :param tone1:
  :param tone2:
  :param sample_rate:
  :param seconds:
  :return:
  """
  combined_tone = makeEmptySound(getLength(tone1))
  for i in range (0, getLength(tone1)):
    first_tone = getSampleValueAt(tone1, i)
    second_tone = getSampleValueAt(tone2, i) 
    setSampleValueAt(combined_tone, i, int(first_tone + second_tone))
  return combined_tone
  

# Algorithm Three: Audio Splice and Swap
def audio_splice(tone1, tone2):
  """ This algorithm plays one tone or sound after the other.
  :param tone1:
  :param tone2:
  :return:
  """
  spliced_length = getLength(tone1) + getLength(tone2)
  spliced = makeEmptySound(spliced_length)
  index = 0
  for source in range(0, getLength(tone1)):
    value = getSampleValueAt(tone1, source)
    setSampleValueAt(spliced, index, value)
    index += 1
  for source in range(0, getLength(tone2)):
    value = getSampleValueAt(tone2, source)
    setSampleValueAt(spliced, index, value)
    index += 1
  return spliced
 
# Algorithm Four: Echo
def echo_sound(delay, sound):
  """ This function takes a sound and then echoes it by however many seconds specified
  :param delay:
  :param sound:
  :return:
  """
  echo = duplicateSound(sound)
  for index in range(delay, getLength(sound)):
    echo_sample = 0.4*getSampleValueAt(echo, (index-delay))
    combined_sample = getSampleValueAt(sound,index) + echo_sample
    setSampleValueAt(sound, index, combined_sample)
  return sound
  

# Algorithm 5: Parsing Tokens into Audio
def note_maker(note_length):
  """ This algorithm generates a melody from a list of notes. Each note has an assigned value that is used to generate a frequency.
  :param note_length:
  :return:
  """
  notes = {'C': -9, 'C#': -8, 'D': -7, 'D#': -6, 'E': -5, 'F':-4, 'F#': -3, 'G': -2, 'G#': -1, 'A': 0, 'A#': 1, 'B': 2, 'c': 3, 'd':4}
  # notes is a dictionary, each note has an assigned value
  melody = ['C', 'D', 'E', 'G', 'A', 'G']
  for n in melody:
    note_number = notes.get(n)
    frequency = 440.0 * 2.0 ** (note_number / 12.0)
    tone = tone_generation(frequency, 4000, note_length)    
    play(tone)
    time.sleep(0.95)        # Changing sleep time changes how much the notes overlap
    
# Algorithm 6: Random Audio Generation
def random_audio(audio_length, note_length):
  """ This algorithm is simlar to note_maker but the value used to generate the frequency with is randomly generated
  :param audio_length:
  :param note_length:
  :return:
  """
  notes = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
  the_tone = makeEmptySoundBySeconds(1)
  seconds = 1
  for n in range(audio_length):
    seconds += 1
    note_number = random.choice(notes)
    frequency = 440.0 * 2.0 **(note_number / 12.0)
    tone = tone_generation(frequency, 4000, note_length)    
    combine = audio_splice(the_tone, tone)
    the_tone = combine
  return combine


def import_audio():
  """ Imports a sound file and converts it into a sound
  :return:
  """
  file = pickAFile()
  sound = makeSound(file)
  return sound


def export_audio(audio):
  """ This function exports the audio as a .wav file so it can be used as gameplay audio
  :param audio:
  :return:
  """
  path = setMediaPath()
  writeSoundTo(audio, 'tone.wav')
  