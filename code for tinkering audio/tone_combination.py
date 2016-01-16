#this function was used to hear the tones individually to know if they had been merged.
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
