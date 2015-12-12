__author__ = 'Hat'


import envelope
import tone
import melody
import sound


def test():
    my_env = envelope.Envelope(0.25, 0.25, 500, 0.25, 0.25)

    fenv = envelope.Envelope(0, 0, 0, 0, 1)

    sine_tone = tone.SineTone(0, 2000, 10, None, fenv)
    square_tone = tone.SquareTone(0, 2000, 10, None, fenv)
    saw_tone = tone.HarmonicSawTone(0, 2000, 10, 10, None, fenv)

    test = sound.Sound()
    saw_tone.add_tone(test)
    test.save("test.wav")

    # upscale = sound.Sound()
    # downscale = sound.Sound()
    #
    # for i in range(13):
    #     square_tone.note = i
    #     square_tone.add_tone(upscale)
    #
    # for i in range(0, -13, -1):
    #     sine_tone.note = i
    #     sine_tone.add_tone(downscale)
    #
    # scale = upscale + downscale
    # scale.echo(5000)
    # scale.save("scale.wav")
    #
    # bah = melody.Melody(120, '4/4')
    # birthday = bah.create_melody("C:4:8 C:4:8 D:4:4 C:4:4 F:4:4 E:4:2 " +
    #                            "C:4:8 C:4:8 D:4:4 C:4:4 G:4:4 F:4:2 " +
    #                            "C:4:8 C:4:8 C:5:4 A:4:4 F:4:4 E:4:4 D:4:2", square_tone)
    # birthday.save("bd.wav")

    short_sound_env = envelope.Envelope(0, 0, 0, 0, 1)
    main_instrument = tone.SquareTone(0, 2000, 0, short_sound_env)
    little_instrument = tone.SquareTone(0, 2000, 0)

    music = melody.Melody(120, '6/8')
    song = music.create_melody("E:3:16 E:3:16 E:3:16 "
                               "B:2:16 B:2:16 B:2:16 "
                               "D:3:16 D:3:16 D:3:16 "
                               "A:2:16 A:2:16 A:2:16 " +
                               "E:3:16 E:3:16 E:3:16 "
                               "B:2:16 B:2:16 B:2:16 "
                               "D:3:16 D:3:16 D:3:16", main_instrument)

    song2 = music.create_melody("E:3:16 E:3:16 E:3:16 "
                               "B:2:16 B:2:16 B:2:16 "
                               "D:3:16 D:3:16 D:3:16 "
                               "A:2:16 A:2:16 A:2:16 " +
                               "A:2:16 Ab:2:16 A:2:16 "
                               "Ab:2:8 Bb:2:16 B:2:16 "
                               "Bb:2:16 B:2:16 C:3:8 B:2:16", main_instrument)

    extra = music.create_melody("E:4:8 D:4:16", little_instrument)
    song.append_sound(extra)
    song.append_sound(song2)
    song.insert_sound_at_time(extra, 3)
    song.insert_sound_at_time(extra, 5)
    song.save("thing.wav")

test()
