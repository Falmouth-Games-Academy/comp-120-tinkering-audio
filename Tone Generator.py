import wave
import struct
import math
import random

# Creates a file to write to
noise_out = wave.open('noise.wav', 'w')

# Creates the parameters of the file
noise_out.setnchannels(1)
noise_out.setsampwidth(2)
noise_out.setframerate(44100)
noise_out.setnframes(44100)
noise_out.setcomptype('NONE', 'not compressed')
Channels = noise_out.getnchannels()


def sine_wave(frequency, volume, attack_time, decay_time, sustain_time, release_time):
    """Envelope function, plays a pure tone but fades into and out of it"""
    # Creates volume_change as a float
    volume_change = 0.00

    # Creates a list for storing all the values
    values = []

    # Sets the sampling rate
    sampling_rate = 44100

    # creates an interval between samples
    if frequency == 0:
        interval = 1
    else:
        interval = 1.0 / frequency
    samples_per_cycle = interval * sampling_rate

    # not sure what that one does
    max_cycle = 2 * math.pi

    # loops for length of the pure tone
    for pos in range((attack_time + decay_time + sustain_time + release_time)):
        # Increases the volume from 0 when in attack time
        if attack_time >= pos:
            volume_change += (float(volume) / float(attack_time))
        # Assigns new value to volume to the sum of 2/3rds of the original value
        if pos == attack_time:
            volume = (float(volume) / 3.0) * 2.0
        # Decreases the volume slightly to 2/3rds in decay time
        if attack_time < pos < attack_time + decay_time:
            volume_change -= (float(volume)/2.0)/decay_time
            # Decreases the volume to 0 when in release time
        if (attack_time + decay_time + sustain_time) <= pos:
            volume_change -= (float(volume) / float(release_time))

        # Creates the sample
        raw_sample = math.sin((pos / samples_per_cycle) * max_cycle)
        value = (int(volume_change * raw_sample))
        values.append(value)

    # Returns the values
    return values


# Dictionary of notes
notes = {
    'BLANK': 0,
    'a': 440.0 * 2.0 ** (0 / 12.0),
    'a#': 440.0 * 2.0 ** (1 / 12.0),
    'b': 440.0 * 2.0 ** (2 / 12.0),
    'c': 440.0 * 2.0 ** (3 / 12.0),
    'c#': 440.0 * 2.0 ** (4 / 12.0),
    'd': 440.0 * 2.0 ** (5 / 12.0),
    'd#': 440.0 * 2.0 ** (6 / 12.0),
    'e': 440.0 * 2.0 ** (7 / 12.0),
    'f': 440.0 * 2.0 ** (8 / 12.0),
    'f#': 440.0 * 2.0 ** (9 / 12.0),
    'g': 440.0 * 2.0 ** (10 / 12.0),
    'g#': 440.0 * 2.0 ** (11 / 12.0),
    'a2': 440.0 * 2.0 ** (12 / 12.0),
}

# sets the volume
note_volume = 8000


def twinkle():
    """" Generates twinkle twinkle little star"""
    # Sets the length of the note in seconds
    note_time = 0.4
    values = []

    # sets the percentage of the notes attack, sustain and decay times, values add up to 1
    attacktime = int((0.1 * note_time) * 44100)
    decaytime = int((0.2 * note_time) * 44100)
    sustaintime = int((0.6 * note_time) * 44100)
    releasetime = int((0.2 * note_time) * 44100)

    # Twinkle in list form
    playnotes = ['c', 'c', 'g', 'g', 'a2', 'a2', 'g', 'BLANK', 'f', 'f', 'e', 'e', 'd', 'd', 'c', 'BLANK', 'g', 'g', 'f', 'f', 'e', 'e', 'd','BLANK', 'g', 'g', 'f', 'f', 'e', 'e', 'd']

    # creates the notes
    for note in range(len(playnotes)):
        note_values = sine_wave(notes[playnotes[note]], note_volume, attacktime, decaytime, sustaintime, releasetime)

        # Appends the list to include new notes
        for i in xrange(len(note_values)):
            values.append(note_values[i])
        drum_values = drum_beat()
        # Appends the list to include drum beat
        for i in xrange(len(drum_values)):
            values.append(drum_values[i])
    # returns the list of values
    return values


def random_tune():
    """ Generates a random tune"""
    for note in range(10):
        note_time = random.choice([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
        attacktime = int((0.1 * note_time) * 44100)
        sustaintime = int((0.6 * note_time) * 44100)
        decaytime = int((0.3 * note_time) * 44100)
        sine_wave(notes[random.choice(['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#'])], note_volume, attacktime, sustaintime, decaytime)

def drum_beat():
    """drum beat work in progress"""
    values = []
    for i in xrange(1000):
        value = math.sin(2.0 * math.pi * 120 * (i/44100.0)) * (0.5 * (2 ** 15 - 1))
        values.append(value)
    return values

def pack_values(values):
    """Packages the and appends the values"""
    output_values = []
    for value in values:
        packaged_value = struct.pack("<h", value)
        for j in xrange(Channels):
            output_values.append(packaged_value)
    value_str = ''.join(output_values)
    noise_out.writeframes(value_str)


values = twinkle()
pack_values(values)

