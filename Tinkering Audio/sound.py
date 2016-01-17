"""Contain a class for storing and manipulating sound.

This module contains a class to be used for creating and manipulating sound.
Sound can be created and managed using this class, and can then be saved as a
wav file.

Classes:
Sound -- class for managing sound
"""


import array
import os
import wave


class Sound(object):

    """Contain methods and fields for storing and processing audio.

    This class contains method for creating and manipulating sound.
    Samples can be added and manipulated before saving the sound as
    a wav file.

    Public methods:
    save -- saves the sound as a wav file
    add_sample -- adds a sample to the sound
    append_sound -- adds a sound to the end of the sound
    insert_sound_at_time -- adds a sound in the middle of the sound
    layer_sound_at_time -- layers a sound over the sound
    set_sample_at_index -- sets the value of the sample at specified index
    combine_sample_at_index -- combines the value of the sample at index with another sample
    repeat -- makes the sound repeat the specified number of times
    reverse -- reverses the sound
    copy -- makes a copy of the Sound instance
    echo -- adds an echo to the sound
    feedback_echo -- adds a feedback echo to the sound
    convert_secs_to_samples -- converts number of seconds to number of samples
    """

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

    def save(self, directory, filename):
        """Save the sound to a wav file of the given filename.

        Arguments:
        directory -- the directory file should be saved in as a string
        filename -- the name of the file + .wav as a string
        """

        sound = wave.open(os.path.join(directory, filename), 'wb')
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
        """Insert a sound at the given time.

        This method inserts the supplied Sound into this Sound instance
        at the time specified in seconds.

        Arguments:
        sound -- sound to be inserted as a Sound
        seconds -- time it should be inserted at
        """

        start_position = seconds * self.sampling_rate
        for i in range(start_position, start_position + len(sound.samples)):
            self.samples.insert(i, sound.samples[i-start_position])

    def layer_sound_at_time(self, sound, seconds):
        """Overlay a sound at the given time.

        This method layers the supplied Sound over this Sound instance
        at the time specified in seconds.

        Arguments:
        sound -- sound to be overlayed as a Sound
        seconds -- time it should be added at
        """

        start_position = int(seconds * self.sampling_rate)
        for i in range(start_position, start_position + len(sound.samples)):
            self.combine_sample_at_index(sound.samples[i - start_position], i)

    def set_sample_at_index(self, value, index):
        """Set the value of the sample at the specified index"""

        self.samples[index] = value

    def combine_sample_at_index(self, value, index):
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
        vol_reduction -- fraction of the original volume that the echo will be (float between 0 and 1)
        """

        echo = Sound()
        echo.samples = self.samples
        for i in range(len(echo.samples)):
            self.combine_sample_at_index(int(vol_reduction * echo.samples[i]), i + delay)

    def feedback_echo(self, delay, vol_reduction):
        """Add an echo effect with feedback to the sound.

        Arguments:
        delay -- amount of time that the echo will be delayed by in seconds
        vol_reduction -- percentage of the original volume that the echo will be (float between 0 and 1)
        """

        for i in range(len(self.samples)):
            self.combine_sample_at_index(int(vol_reduction * self.samples[i]), i + delay)

    def convert_secs_to_samples(self, seconds):
        """Convert seconds into sample number and return as an integer.

        Arguments:
        seconds -- the number of seconds to convert"""

        return int(self.sampling_rate * seconds)

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
