__author__ = 'Hat'

import os

import filter
import envelope
import melody
import sound
import tone

OUTPUT_DIR = 'output'

# Temporary function for testing purposes and experimentation
def test():
    new = sound.Sound()

    fenv = envelope.Envelope(envelope.EnvelopeType.frequency, -1, 0.25, 0.25, 0.25, 0.25)

    filt = filter.Peaking(new, 5000, 1, 1)
    noise = tone.Noise(0, 2000, 5, filt, None, fenv)

    noise.add_tone(new)

    new.save(OUTPUT_DIR, "testy.wav")



    # my_env = envelope.Envelope(0.25, 0.25, 500, 0.25, 0.25)
    #
    # fenv = envelope.Envelope(0, 0, 0, 0, 1)
    #
    # sine_tone = tone.SineTone(0, 2000, 10, None, fenv)
    # square_tone = tone.SquareTone(0, 2000, 10, None, fenv)
    # saw_tone = tone.HarmonicSawTone(0, 2000, 10, 10, None, fenv)
    #
    # test = sound.Sound()
    # saw_tone.add_tone(test)
    # test.save("test.wav")
    #
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


def make_bg_music():

    # The entire sound is release phase to make it fade out quickly
    short_sound_env = envelope.Envelope(envelope.EnvelopeType.amplitude, 0, 0, 0, 0, 1)

    main_instrument = tone.SquareTone(0, 1000, 0, short_sound_env)
    little_instrument = tone.SquareTone(0, 1000, 0)

    # 120bpm, 6/8 compound time signature to emulate triplets
    music = melody.Melody(120, '6/8')

    first_bar_string = ("E:3:16 E:3:16 E:3:16 "
                       "B:2:16 B:2:16 B:2:16 "
                       "D:3:16 D:3:16 D:3:16 "
                       "A:2:16 A:2:16 A:2:16 ")

    first_part = music.create_melody(first_bar_string +
                                     "E:3:16 E:3:16 E:3:16 "
                                     "B:2:16 B:2:16 B:2:16 "
                                     "D:3:16 D:3:16 D:3:16", main_instrument)

    second_part = music.create_melody(first_bar_string +
                                      "A:2:16 Ab:2:16 A:2:16 "
                                      "Ab:2:8 Bb:2:16 B:2:16 "
                                      "Bb:2:16 B:2:16 C:3:8 B:2:16", main_instrument)

    extra_bit = music.create_melody("E:4:8 D:4:16", little_instrument)

    # Time that the extra bit should be overlayed
    overlap_time = music.get_time_at_beat(10.5)

    first_part.append_sound(extra_bit)
    second_part.layer_sound_at_time(extra_bit, overlap_time)

    intro = first_part.copy()
    intro.repeat(2)
    intro.append_sound(second_part)

    main_part = first_part.copy()
    main_part.append_sound(second_part)

    main_part.repeat(3)

    song = intro.copy()
    song.append_sound(main_part)

    song.save(OUTPUT_DIR, "song.wav")


def make_eating_sound():
    # These are just arbitrary numbers that I played around with until it sounded good
    chomp_fenv = envelope.Envelope(envelope.EnvelopeType.frequency, -5, 0.5, 0.5, 0, 0)
    chomp_env = envelope.Envelope(envelope.EnvelopeType.amplitude, 0, 0, 0, 0.5, 0.5)

    chomp_high = sound.Sound()
    # -17 makes tone play a low E
    chomp_tone_high = tone.SquareTone(-17, 2000, 0.1, chomp_env, chomp_fenv)

    chomp_low = sound.Sound()
    # -22 makes tone play the B below the previous E
    chomp_tone_low = tone.SquareTone(-22, 2000, 0.1, chomp_env, chomp_fenv)

    chomp_tone_high.add_tone(chomp_high)
    chomp_tone_low.add_tone(chomp_low)

    chomp_high.save(OUTPUT_DIR, "chomp_high.wav")
    chomp_low.save(OUTPUT_DIR, "chomp_low.wav")

def make_start_sound():

    jingle_env = envelope.Envelope(envelope.EnvelopeType.amplitude, 0, 0, 0, 0, 1)
    instrument = tone.SquareTone(0, 2000, 0, jingle_env)

    # 120bpm, 6/8 compound time signature to emulate triplets
    music = melody.Melody(120, '6/8')
    jingle = music.create_melody("C:2:8 C:2:16 D:2:8 C:2:16 "
                                 "Eb:2:8 C:2:4 F#:2:6 F#:2:8 G:2:2", instrument)

    jingle.save(OUTPUT_DIR, "jingle.wav")

def make_death_sound():
    pass

def make_powerup_sound():
    pass


def make_frightened_sound():
    frightened_fenv = envelope.Envelope(envelope.EnvelopeType.frequency, -3, 0.25, 0.25, 0.25, 0.25)
    frightened_aenv = envelope.Envelope(envelope.EnvelopeType.amplitude, 1786, 0.25, 0.25, 0.25, 0.25)
    frightened_tone = tone.SineTone(25, 2000, 1, None, frightened_fenv)

    frightened_sound = sound.Sound()
    frightened_tone.add_tone(frightened_sound)

    frightened_fenv.file.close()

    frightened_sound.save(OUTPUT_DIR, "frightened.wav")


def make_retreating_sound():
    retreat_fenv = envelope.Envelope(envelope.EnvelopeType.frequency, 0, 1, 0, 0, 0)
    retreat_tone = tone.SineTone(25, 2000, 1.5, None, retreat_fenv)

    retreat_sound = sound.Sound()
    retreat_tone.add_tone(retreat_sound)

    retreat_sound.feedback_echo(5000, 0.6)

    retreat_sound.save(OUTPUT_DIR, "retreat.wav")


if __name__ == '__main__':
    test()
    make_eating_sound()
    make_start_sound()
    make_frightened_sound()
    make_retreating_sound()