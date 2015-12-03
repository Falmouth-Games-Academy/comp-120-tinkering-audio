__author__ = 'Hat'


import array
import math
import wave

import tone
import melody
import sound


def test():
    sine_tone = tone.SineTone(0, 2000, 0.25)
    square_tone = tone.SquareTone(0, 2000, 0.5)
    upscale = sound.Sound()
    downscale = sound.Sound()

    for i in range(13):
        square_tone.note = i
        square_tone.add_tone(upscale)

    for i in range(0, -13, -1):
        sine_tone.note = i
        sine_tone.add_tone(downscale)

    scale = upscale + downscale
    scale.echo(10000)
    scale.save("scale.wav")

    bah = melody.Melody(120, '4/4')
    birthday = bah.create_melody("C:8 C:8 D:4 C:4 F:4 E:2 " +
                               "C:8 C:8 D:4 C:4 G:4 F:2 " +
                               "C:8 C:8 c:4 A:4 F:4 E:4 D:2", square_tone)
    birthday.save("bd.wav")

    tune = melody.Melody(240, '12/8')
    thing = tune.create_melody("e:4 B:4 d:4 A:4 " +
                               "e:4 B:4 d:2", square_tone)

    thing.save("thing.wav")

test()
