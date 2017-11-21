import pygame as pg
import numpy
import wave
import math
import struct
'''pg.init()
pg.mixer.init()

pg.display.set_mode((800,600))
# load in some music (filename)
pg.mixer.music.load('410735__greek555__sample-126-bpm')

# plays the music for (loops, start)
pg.mixer.music.play()

# sets an sound to an variable
expolision_sound = pg.mixer.Soundound('410735__greek555__sample-126-bpm')

# takes in an sound and give an array of samples
expolision_samples= pg.sndarray.samples('410735__greek555__sample-126-bpm')

#prints out samples
for sample in expolision_samples:
    print (sample)

# go though a list of samples and then does somehthing
def change_volume(samples,colume_change):
    for samples in sample:
'''
song ='410735__greek555__sample-126-bpm'
SAMPLE_LENGTH = 93
FREQUENCY = 500
SAMPLE_RATE = 50
VOLUME= 50
BIT_DEPTH = 32000
CHANNELS = 2

noise_out = wave.open(song,'w')
values = []
for i in range(0, SAMPLE_LENGTH):
    value = math.sin(2.0 * math.pi*FREQUENCY*( i / SAMPLE_RATE)) * (VOLUME * BIT_DEPTH)

    packaged_value = struct.pack('<h', value)

    for j in xrange(0, CHANNELS):
        values.append(packaged_value)

value_str = ''.join(values)
noise_out.write(value_str)
noise_out.close()


done = False
while not done:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            done=True
        '''if event.key == pg.K_SPACE:
            # plays a sound (-1) make it play forever
            expolision_sound.play()
 #       if event.key ==pg.K_UP'''
    pg.display.set_mode((800, 600))

pg.quit()