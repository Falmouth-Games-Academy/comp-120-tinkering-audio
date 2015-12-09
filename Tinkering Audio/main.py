__author__ = 'Hat'


import tone
import melody
import sound


def test():
    sine_tone = tone.SineTone(0, 2000, 0.5)
    square_tone = tone.SquareTone(0, 2000, 0.5)
    saw_tone = tone.HarmonicSawTone(0, 2000, 0.5, 10)


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

    # bah = melody.Melody(120, '4/4')
    # birthday = bah.create_melody("C:4:8 C:4:8 D:4:4 C:4:4 F:4:4 E:4:2 " +
    #                            "C:4:8 C:4:8 D:4:4 C:4:4 G:4:4 F:4:2 " +
    #                            "C:4:8 C:4:8 C:5:4 A:4:4 F:4:4 E:4:4 D:4:2", square_tone)
    # birthday.save("bd.wav")

    tune = melody.Melody(240, '12/8')
    high = tune.create_melody("E:5:4 B:4:4 D:5:4 A:4:4 " +
                              "E:5:4 B:4:4 D:5:2", saw_tone)
    low = tune.create_melody("E:4:4 B:3:4 D:4:4 A:3:4 " +
                             "E:4:4 B:3:4 D:4:2", saw_tone)

    song = low + high
    song.save("thing.wav")

    low.save("test.wav")




test()
