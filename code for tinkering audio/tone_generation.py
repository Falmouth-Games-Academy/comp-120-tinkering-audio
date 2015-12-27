#function for generating a tone.
def toneGeneration():
    secs = 5                                                  #setting the length, frequencey and amplitude of the clip.
    freq = 150
    amplitude = 3000
    buildSin = makeEmptySoundBySeconds(secs)                  #building the clip
    sampleRate = getSamplingRate(buildSin)
    interval = 1.0/freq
    samplesPerCycle = interval * sampleRate                   #working out the samples per cycle.
    maxCycle = 2 * pi
    for pos in range (0,getLength(buildSin)):
        rawSample = sin((pos / samplesPerCycle) * maxCycle)   
        sampleValue = int(amplitude * rawSample)              #gets the value of the sample.
        setSampleValueAt(buildSin, pos, sampleValue)          #sets that value to be played for the length of the clip.
    play(buildSin)
    