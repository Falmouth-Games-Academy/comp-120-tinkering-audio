#Random audio generation.

import random

def randomAudio():
  S1 = makeEmptySoundBySeconds(15)
  intensity = 64
  dur = 1000
  a = playNote(56, dur, intensity)
  b = playNote(58, dur, intensity)
  c = playNote(60, dur, intensity)
  d = playNote(62, dur, intensity)
  e = playNote(64, dur, intensity)
  f = playNote(66, dur, intensity)
  g = playNote(68, dur, intensity)
  h = playNote(70, dur, intensity)
  i = playNote(72, dur, intensity)
  j = playNote(74, dur, intensity)
  for x in range (1, 30):
    notes = ["a","b","c","d","e","f","g","h","i","j","k","l"]
    play random.choice(notes)
    
#doesnt work.
  