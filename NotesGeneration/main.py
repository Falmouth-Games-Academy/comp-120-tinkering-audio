from notes import *
from noteFrequencies import *
import winsound, wave, struct, sys, pygame,random
from pygame.locals import *


pygame.init()
# function to play note (takes string for note name)
def play(note, identifyer):
    winsound.PlaySound(str('Notes/' + str(note) + '_' + identifyer + '.wav'), winsound.SND_FILENAME)

# this will generate all the notes so only needs to run the first time

# Note(RandomNote, sampleRate, samplelength, bitDepth, volume)
#
# play(RandomNote)
melody = []
chorus = []
notemarker = 0


def Generate_song(melody, chorus, notemarker):
    # melody = []
    # chorus = []
    # notemarker = 0
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


print 'press g to generate song'
print 'press c to play Cool Plane Sound'
print 'press 1 to write random note to melody1.wav'
print 'press 2 to write random note to melody2.wav'
print 'press enter to save melodys'

Width = 300
Height = 200
window = pygame.display.set_mode((Width, Height), 0, 32)
pygame.display.set_caption('Press keys in this window')



while True:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if keys[K_g]:
            Generate_song(melody, chorus, notemarker)
            print 'press space to play once'
            print 'press i to play infinitely'
        if keys[K_i]:
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
        if keys[K_SPACE]:
            for song in xrange(1):
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
                print 'press space to play song'
                print 'press i to play song infinitely'
                print 'press 1 to write random note to melody1.wav'
                print 'press 2 to write random note to melody2.wav'
                print 'press enter to save melody1.wav'
                print 'press keypad enter to save melody2.wav'

        if keys[K_1]:
            print "added random notes to melody1.wav"
            randomnote(values, noise_out)
        if keys[K_RETURN]:
            print 'melodys saved'
            savesound(noise_out)
            savesound(noise_out2)
        if keys[K_2]:
            print "added random notes to melody2.wav"
            randomnote(values2, noise_out2)
        if keys[K_3]:
            randomnote(values, noise_out)
            cool_plane_sound()
            print 'CoolPlaneSound.wav saved'
            winsound.PlaySound('CoolPlaneSound.wav', winsound.SND_FILENAME)

