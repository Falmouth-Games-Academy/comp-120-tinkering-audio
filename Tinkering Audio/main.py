__author__ = 'Hat'

# Standard Python library
import os

# Own modules
import filter
import envelope
import melody
import sound
import tone


OUTPUT_DIR = 'output'


def create_gameplay_audio():
    make_eating_sound()
    make_start_sound()
    make_frightened_sound()
    make_retreating_sound()
    make_death_sound()


def make_bg_music():
    """Produce a song to be used for the title screen."""

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

    background = music.create_melody("E:4:12 B:4:12 D:4:12 A:4:12 E:4:12 B:3:12 D:4:12")

    # Time that the extra bit should be overlayed
    overlap_time = music.get_time_at_beat_of_bar(2, 4.5)

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
    """Create sounds to be used for collecting a pellet."""

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
    """Create a sound to be used when the game begins."""

    # Entire tone is release phase to make it fade out quickly
    jingle_env = envelope.Envelope(envelope.EnvelopeType.amplitude, 0, 0, 0, 0, 1)
    instrument = tone.SquareTone(0, 2000, 0, jingle_env)

    # 120bpm, 6/8 compound time signature to emulate triplets
    music = melody.Melody(120, '6/8')
    jingle = music.create_melody("C:2:8 C:2:16 D:2:8 C:2:16 "
                                 "Eb:2:8 C:2:4 F#:2:6 F#:2:8 G:2:2", instrument)

    jingle.save(OUTPUT_DIR, "jingle.wav")


def make_death_sound():
    """Create a sound to be played upon death."""

    # Entire tone is release phase to make it fade out quickly
    death_env = envelope.Envelope(envelope.EnvelopeType.amplitude, 0, 0, 0, 0, 1)
    instrument = tone.SquareTone(0, 2000, 0, death_env)

    # 120bpm, 6/8 compound time signature to emulate triplets
    music = melody.Melody(120, '6/8')
    death = music.create_melody("F#:2:6 F#:2:8 G:2:6 F:2:16 Eb:2:8 D:2:16 C:2:4", instrument)

    death.save(OUTPUT_DIR, "death.wav")


def make_powerup_sound():
    """Create a sound to be played when a power-up is collected."""

    pass


def make_frightened_sound():
    """Create a sound to be played when the enemy is frightened."""

    frightened_fenv = envelope.Envelope(envelope.EnvelopeType.frequency, -3, 0.25, 0.5, 0, 0.25)
    frightened_aenv = envelope.Envelope(envelope.EnvelopeType.amplitude, 0, 0, 0.9, 0, 0.1)
    frightened_tone = tone.SineTone(31, 2000, 0.5, frightened_aenv, frightened_fenv)

    music = melody.Melody(240, '4/4')

    notes = "D:4:8 Eb:4:8 C:4:8 F#:4:8 G:4:8 "
  # notes = "E:4:8 C:4:8 B:4:8 Eb:4:8 G:4:8 "
    # So that notes can be used more than once (arbitrary number)
    notes *=5
    frightened_sound = music.create_shuffled_melody(notes, frightened_tone)
    # Sound should last a while (arbitrary number)
    frightened_sound.repeat(5)

    frightened_sound.save(OUTPUT_DIR, "frightened.wav")

    frightened_fenv.file.close()


def make_retreating_sound():
    """Create a sound to be played when the enemy is retreating."""

    retreat_fenv = envelope.Envelope(envelope.EnvelopeType.frequency, 0, 1, 0, 0, 0)
    retreat_tone = tone.SineTone(25, 2000, 1.5, None, retreat_fenv)

    retreat_sound = sound.Sound()
    retreat_tone.add_tone(retreat_sound)

    retreat_sound.feedback_echo(5000, 0.6)

    retreat_sound.save(OUTPUT_DIR, "retreat.wav")


if __name__ == '__main__':
    create_gameplay_audio()
