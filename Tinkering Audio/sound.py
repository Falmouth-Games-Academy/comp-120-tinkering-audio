__author__ = 'Hat'

import array
import math
import wave


class Sound(object):
    def __init__(self, channels=1, sample_width=2, sampling_rate=44100):
        """Initialises the fields and sets up an empty wav file

        Arguments:
        samples =
        channels -- number of channels. Defaults to 1 (mono)
        sample_width -- sample width in bytes. Defaults to 2 (16-bit)
        sampling_rate -- samples per second. Defaults to 44100 (CD quality)
        """
        self.samples = None
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
            for sample in data:
                samples.append(sample)
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
        """Save the sound to a wav file of the given filename"""
        sound = wave.open(filename, 'wb')
        sound.setnchannels(self.channels)
        sound.setsampwidth(self.sample_width)
        sound.setframerate(self.sampling_rate)
        sound.writeframes(self.samples.tostring())
        sound.close()

    def add_sample(self, value):
        """Add the sample to the end of the sound"""
        self.samples.append(value)

    def append_sound(self, sound):
        for sample in sound.samples:
            self.samples.append(sample)

    def set_sample_at_index(self, value, index):
        """Set the sample at the specified index"""
        self.samples[index] = value

    def combine_sample(self, index, value):
        """Add the value to the sample at the specified index"""
        if len(self.samples) > index:
            self.samples[index] += value
        else:
            self.add_sample(value)

    def reverse(self):
        self.samples.reverse()

    def copy(self):
        """Return a copy of the sound object as a new instance"""
        sound = Sound()
        sound.samples = self.samples
        sound.channels = self.channels
        sound.sampling_rate = self.sampling_rate
        sound.sample_width = self.sample_width
        return sound

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

    def echo(self, delay):
        echo = Sound()
        echo.samples = self.samples
        for i in range(len(echo.samples)):
            self.combine_sample(i + delay, int(0.6 * echo.samples[i]))

