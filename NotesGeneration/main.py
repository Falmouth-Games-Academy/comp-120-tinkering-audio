from notes import *
import winsound, pygame

# function to play note (takes string for note name)
def play(note, identifyer):
    winsound.PlaySound(str('Notes/' + str(note) + '_' + identifyer + '.wav'), winsound.SND_FILENAME)

# this will generate all the notes so only needs to run the first time

# Note(RandomNote, sampleRate, sampleLength, bitDepth, volume)
#
# play(RandomNote)
melody = []
chorus = []
notemarker = 0

for i in xrange(2):
    for i in xrange(8):
        notemarker += 1
        samplelength = 44100 / (i + 1)
        noteChoice = notegen()
        noteInput = (noteChoice, notes[noteChoice])
        print noteInput
        Note(noteInput, sampleRate, samplelength, bitDepth, volume, ('melody' + str(notemarker)))
        melody.append(noteChoice)

for i in xrange(8):
    samplelength = 44100 / 16
    noteChoice = notegen()
    noteInput = (noteChoice, notes[noteChoice])
    print noteInput
    Note(noteInput, sampleRate, samplelength, bitDepth, volume, 'chorus')
    chorus.append(noteChoice)

while True:

    for i in xrange(4):
        print 'melody'
        j = 0
        for pitch in melody:
            j += 1
            play(pitch, ('melody' + str(j)))
        j = 0

    for i in xrange(3):
        for times in xrange(3):
            print 'chorus'
            for pitch in chorus:
                print times
                for i in xrange(times):
                    play(pitch, 'chorus')