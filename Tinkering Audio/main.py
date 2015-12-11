__author__ = 'Hat'


import envelope
import tone
import melody
import sound


def test():
    my_env = envelope.Envelope(0, 0, 1500, 0, 1)
    sine_tone = tone.SineTone(0, 2000, 0.5, my_env)
    square_tone = tone.SquareTone(0, 2000, 0.5, my_env)
    saw_tone = tone.HarmonicSawTone(0, 2000, 0.5, 10, my_env)


    upscale = sound.Sound()
    downscale = sound.Sound()

    for i in range(13):
        square_tone.note = i
        square_tone.add_tone(upscale)

    for i in range(0, -13, -1):
        sine_tone.note = i
        sine_tone.add_tone(downscale)

    scale = upscale + downscale
    scale.echo(5000)
    scale.save("scale.wav")

    bah = melody.Melody(120, '4/4')
    birthday = bah.create_melody("C:4:8 C:4:8 D:4:4 C:4:4 F:4:4 E:4:2 " +
                               "C:4:8 C:4:8 D:4:4 C:4:4 G:4:4 F:4:2 " +
                               "C:4:8 C:4:8 C:5:4 A:4:4 F:4:4 E:4:4 D:4:2", square_tone)
    birthday.save("bd.wav")



    music = melody.Melody(120, '6/8')
    song = music.create_melody("E:3:16 E:3:16 E:3:16 "
                               "B:2:16 B:2:16 B:2:16 "
                               "D:3:16 D:3:16 D:3:16 "
                               "A:2:16 A:2:16 A:2:16 " +
                               "E:3:16 E:3:16 E:3:16 "
                               "B:2:16 B:2:16 B:2:16 "
                               "D:3:16 D:3:16 D:3:16", square_tone)

    song.save("thing.wav")

test()
