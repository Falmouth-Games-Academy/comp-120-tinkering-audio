#function for generating a tone.

def toneGeneration(sec, freq, amplitude):
    buildSin = makeEmptySoundBySeconds(secs)                  #building the clip
    sampleRate = getSamplingRate(buildSin)
    interval = 1.0/freq
    samplesPerCycle = interval * sampleRate                   #working out the samples per cycle.
    maxCycle = 2 * pi
    for pos in range (0,getLength(buildSin)):
        rawSample = sin((pos / samplesPerCycle) * maxCycle)   
        sampleValue = int(amplitude * rawSample)              #gets the value of the sample.
        setSampleValueAt(buildSin, pos, sampleValue)          #sets the value of the tone.
    play(buildSin)
    