"""Contain a class for storing and manipulating sound.

This module contains a class to be used for creating and manipulating sound.
Sound can be created and managed using this class, and can then be saved as a
wav file.

Classes:
Sound -- class for managing sound
"""

import array
import math
import wave


class Sound(object):
    def __init__(self, channels=1, sample_width=2, sampling_rate=44100, samples=None):
        """Initialise the fields.

        Arguments:
        channels -- number of channels. Defaults to 1 (mono)
        sample_width -- sample width in bytes. Defaults to 2 (16-bit)
        sampling_rate -- samples per second. Defaults to 44100 (CD quality)
        samples -- list of samples that the sound should begin with. Defaults to None.
        """
        self.samples = samples
        self.sample_width = sample_width
        self.channels = channels
        self.sampling_rate = sampling_rate

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, data):
        self.__sound = data

    @property
    def samples(self):
        return self.__samples

    @samples.setter
    def samples(self, data):
        # Array of signed short ints
        samples = array.array('h')
        if data != None:
            samples.extend(data)
        self.__samples = samples

    @property
    def channels(self):
        return self.__channels

    @channels.setter
    def channels(self, number):
        self.__channels = number

    @property
    def sample_width(self):
        return self.__sample_width

    @sample_width.setter
    def sample_width(self, size):
        self.__sample_width = size

    @property
    def sampling_rate(self):
        return self.__sampling_rate

    @sampling_rate.setter
    def sampling_rate(self, rate):
        self.__sampling_rate = rate

    def save(self, filename):
        """Save the sound to a wav file of the given filename."""

        sound = wave.open(filename, 'wb')
        sound.setnchannels(self.channels)
        sound.setsampwidth(self.sample_width)
        sound.setframerate(self.sampling_rate)
        sound.writeframes(self.samples.tostring())
        sound.close()

    def add_sample(self, value):
        """Add the sample to the end of the sound."""

        self.samples.append(value)

    def append_sound(self, sound):
        """Add another sound to the end of the sound."""

        self.samples.extend(sound.samples)

    def insert_sound_at_time(self, sound, seconds):
        start_position = seconds * self.sampling_rate
        for i in range(start_position, start_position + len(sound.samples)):
            self.samples.insert(i, sound.samples[i-start_position])

    def layer_sound_at_time(self, sound, seconds):
        start_position = int(seconds * self.sampling_rate)
        for i in range(start_position, start_position + len(sound.samples)):
            self.combine_sample(sound.samples[i - start_position], i)

    def set_sample_at_index(self, value, index):
        """Set the value of the sample at the specified index"""
        self.samples[index] = value

    def combine_sample(self, value, index):
        """Add the value to the sample at the specified index"""
        if len(self.samples) > index:
            self.samples[index] += value
        else:
            self.add_sample(value)

    def repeat(self, repeats):
        """Make the sound be repeated.

        This method appends a copy of the sound to the
        end the specified number of times.

        repeats -- number of additional times sound should repeat
        """
        original_sound = self.copy()
        for i in range(repeats):
            self.append_sound(original_sound)

    def reverse(self):
        """Reverse the sound."""

        self.samples.reverse()

    def copy(self):
        """Return a copy of the sound object as a new instance."""

        sound = Sound(self.channels, self.sample_width,
                      self.sampling_rate, self.samples)
        return sound

    def echo(self, delay, vol_reduction):
        """Add an echo effect to the sound.

        Arguments:
        delay -- amount of time that the echo will be delayed by in seconds
        vol_reduction -- percentage of the original volume that the echo will be
        """

        echo = Sound()
        echo.samples = self.samples
        for i in range(len(echo.samples)):
            self.combine_sample(int(vol_reduction * echo.samples[i]), i + delay)

    def feedback_echo(self, delay, vol_reduction):
        """Add an echo effect with feedback to the sound.

        Arguments:
        delay -- amount of time that the echo will be delayed by in seconds
        vol_reduction -- percentage of the original volume that the echo will be
        """

        for i in range(len(self.samples)):
            self.combine_sample(int(vol_reduction * self.samples[i]), i + delay)

    def __add__(self, other):
        sound = Sound()
        if len(self.samples) >= len(other.samples):
            sound.samples = self.samples
            for i in range(len(other.samples)):
                sound.samples[i] += other.samples[i]
        else:
            sound.samples = other.samples
            for i in range(len(self.samples)):
                sound.samples[i] += self.samples[i]
        return sound
