def makeNoise(freq, amplitude, attack_time, sustain_time, release_time):
 length = int(attack_time + sustain_time + release_time)
 makeTone = makeEmptySoundBySeconds(length)
 samplingRate = getSamplingRate(makeTone)
 the_time1 = int(samplingRate * attack_time)
 the_time2 = int(samplingRate * sustain_time) + the_time1
 the_time3 = int(samplingRate * release_time) + the_time2
 interval = 1.0 / freq
 samplesPerCycle = interval * samplingRate
 maxCycle = 2 * pi
 ADSR = 1
 for pos in range(the_time1):
   rawSample = sin((pos / samplesPerCycle) * maxCycle)
   sampleVal = int(amplitude * rawSample) * ADSR # change to change volume
   setSampleValueAt(makeTone, pos, sampleVal)
   ADSR += 1
   #print sampleVal
 play(makeTone)
 return makeTone