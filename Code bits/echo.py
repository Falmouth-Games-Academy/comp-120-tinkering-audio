def echo(sound1, sound2, second_delay):
  for i in range(second_delay, getLength(sound1)):
    echo = 0.6*getSampleValueAt(sound2, i-second_delay)
    combo = getSampleValueAt(sound1, i) + echo
    setSampleValueAt(sound1, i, combo)
  play(sound1)
  return sound1