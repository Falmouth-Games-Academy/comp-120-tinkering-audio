#this function was used to hear the tones individually to know if they had been merged.
def sound():
  file = makeSound(pickAFile())
  play(file)
  
#this function takes the sound files and merges them together. 
def toneCombination():
  sound1 = makeSound(pickAFile())
  sound2 = makeSound(pickAFile())
  canvas = makeEmptySoundBySeconds(5)
  for index in range(0, getLength(sound1)):
    combinationSoundSample1 = getSampleValueAt(sound1, index)
  for index in range(0, getLength(sound2)):
    combinationSoundSample2 = getSampleValueAt(sound2, index)
    setSampleValueAt(canvas, index, combinationSoundSample1 + combinationSoundSample2)
  play(canvas)
  return canvas
