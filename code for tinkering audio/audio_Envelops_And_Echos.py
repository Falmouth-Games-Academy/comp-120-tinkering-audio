#audio envelops and echos.

def echoes(delay, num):
  sound = makeSound(pickAFile())
  s1 = getLength(sound)
  s2 = s1 + (delay * num)
  canvas = makeEmptySound(s2)
  
  echoAmplitude = 1.0
  for echoCount in range(1, num):
    echoAmplitude = echoAmplitude * 0.6
    for posns1 in range(0, s1):
      posns2 = posns1 + ( delay * echoCount)
      values1 = getSampleValueAt (sound, posns1) * echoAmplitude
      values2 = getSampleValueAt(canvas, posns2)
      setSampleValueAt(canvas, posns2, values1 + values2)
  play(canvas)