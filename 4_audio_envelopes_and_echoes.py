""" The first function chooses a file and turns into a sound file ready for use in the second function"""
def soundFile():
  theSound = pickAFile()
  soundFile = makeSound(theSound)
  play(soundFile)
  return soundFile

"""This function takes a sound and then echoes it by however many seconds specified"""
def echo(sound1, sound2, second_delay):
  #echo_length = getLength(sound1) + (second_delay* getSamplingRate(sound1)
  for i in range(int(second_delay), getLength(sound1)):
    echo = 0.4*getSampleValueAt(sound2, i-int(second_delay))
    combo = getSampleValueAt(sound1, i) + echo
    setSampleValueAt(sound1, i, combo)
  play(sound1)
  return sound1
