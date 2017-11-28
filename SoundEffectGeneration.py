import wave
import math
import struct
import random

SAMPLE_WIDTH = random.randint(2, 4)
SAMPLE_RATE = 44100.0
BIT_DEPTH = 2.0
CHANNELS = 2

'''when running this file it will create/alter the Echo.wav, tone1.wav, tone2.wav and tone3.wav file to
contain the new sounds that was just created by running this'''


# combines the two tones into one sample


def combine_tones(tone_one, tone_two, sample_length):
    values = []
    for i in range(0, sample_length):
        values.append(tone_one[i]+tone_two[i])
    return values


# Generates a new sine wave based on the constants above


def generate_sine_wave(frequency, sample_rate, sample_length, volume):
    values = []
    for i in range(0, sample_length):
        value = math.sin(2 * math.pi * frequency * (i / sample_rate)) * (volume * BIT_DEPTH)
        for j in xrange(0, CHANNELS):
            values.append(value)

    return values


# here the new sound gets saved as a wav file


def save_wave_file(filename, wav_data, sample_rate):
    packed_values = []
    for i in range(0, len(wav_data)):
        packed_value = struct.pack('h', wav_data[i])
        packed_values.append(packed_value)

    noise_out = wave.open(filename, 'w')
    noise_out.setparams((CHANNELS, SAMPLE_WIDTH, sample_rate, 0, 'NONE', 'not compressed'))
    value_str = ''.join((str(n) for n in packed_values))
    noise_out.writeframes(value_str)
    noise_out.close()


# This creates a simple echo like file by adding the sound to itself


def sound_effect(sound1, sound2, sound3, delay, sample_length):
    values = []
    for i in range(0, sample_length):
        values.append(sound1[i])
        if i > delay:
            echo = sound2[i]*0.6
            values.append(echo+sound1[i])
        if i > delay*2:
            echo2 = sound3[i]*0.6
            values.append(echo2 + sound2[1] + sound1[i])
    return values

# setting each of the tone values

tone_values_one = generate_sine_wave(random.randint(3000.0, 5000.0),
                                     SAMPLE_RATE,
                                     random.randint(102000, 142000),
                                     random.randint(500.0, 10000.0))

tone_values_two = generate_sine_wave(random.randint(3000.0, 5000.0),
                                     SAMPLE_RATE,
                                     random.randint(102000, 142000),
                                     random.randint(500.0, 10000.0))

tone_values_three = generate_sine_wave(random.randint(30.0, 100.0),
                                       SAMPLE_RATE,
                                       random.randint(102000, 142000),
                                       random.randint(500.0, 10000.0))


# save all files

save_wave_file('sound_effect1.wav', tone_values_one, SAMPLE_RATE)
save_wave_file('sound_effect2.wav', tone_values_two, SAMPLE_RATE)
save_wave_file('sound_effect3.wav', tone_values_three, SAMPLE_RATE)

echo_values = sound_effect(tone_values_one, tone_values_two, tone_values_three, 40000, 132000)

save_wave_file('combined_sound_effect.wav', echo_values, SAMPLE_RATE)
