__author__ = 'Hat'


import array
import math
import wave


class Sound(object):
    def __init__(self, filename, channels=1, sample_width=2, sampling_rate=44100):
        """Initialises the fields and sets up an empty wav file

        Arguments:
        filename -- the name/path of the file that the new
        sound will be saved in as a string
        channels -- number of channels. Defaults to 1 (mono)
        sample_width -- sample width in bytes. Defaults to 2 (16-bit)
        sampling_rate -- samples per second. Defaults to 44100 (CD quality)
        """
        self.sound = wave.open(filename, 'wb')
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
        self.sound.setnchannels(self.channels)

    @property
    def sample_width(self):
        return self.__sample_width

    @sample_width.setter
    def sample_width(self, size):
        self.__sample_width = size
        self.sound.setsampwidth(self.sample_width)

    @property
    def sampling_rate(self):
        return self.__sampling_rate

    @sampling_rate.setter
    def sampling_rate(self, rate):
        self.__sampling_rate = rate
        self.sound.setframerate(self.sampling_rate)

    def save(self):
        self.sound.writeframes(self.samples.tostring())
        self.sound.close()

    def add_sample(self, value):
        self.samples.append(value)

    def __add__(self, other):
        size = min(len(self.samples), len(other.samples))
        for i in range(size):
            self.samples[i] += other.samples[i]
        return self.samples


class Tone:
    def generate(self, filename):
        raise NotImplementedError


class SineTone(Tone):
    def __init__(self, frequency, amplitude, seconds):
        self.frequency = frequency
        self.amplitude = amplitude
        self.seconds = seconds

    def generate(self, sound):
        seconds_per_cycle = 1.0/self.frequency
        samples_per_cycle = seconds_per_cycle * sound.sampling_rate
        max_cycle = 2 * math.pi

        for i in xrange(sound.sampling_rate * self.seconds):
            sample = int((math.sin((i / samples_per_cycle) * max_cycle)) * self.amplitude)
            sound.add_sample(sample)


class SquareTone(Tone):
    def __init__(self, frequency, amplitude, seconds):
        self.frequency = frequency
        self.amplitude = amplitude
        self.seconds = seconds

    def generate(self, sound):
        interval = 1.0/self.frequency
        samples_per_cycle = interval * sound.sampling_rate

        sample = self.amplitude
        position = 0
        for i in xrange(sound.sampling_rate * self.seconds):
            if position > int(samples_per_cycle/2):
                sample *= -1
                position = 0
            sound.add_sample(sample)
            position += 1


def test():
    sine = SineTone(880, 2000, 5)
    sine_tone = Sound("foo.wav")
    sine.generate(sine_tone)

    square = SquareTone(440, 2000, 5)
    square_tone = Sound("bar.wav")
    square.generate(square_tone)

    square_tone + sine_tone
    new_sound = Sound("bah.wav")
    new_sound.samples = square_tone + sine_tone
    new_sound.save()


test()
