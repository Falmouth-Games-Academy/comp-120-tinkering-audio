__author__ = 'Hat'


import array
import math
import wave


class Sound(object):
    def __init__(self, filename, samples=None, channels=1, sample_width=2, sampling_rate=44100):
        """Initialises the fields and sets up an empty wav file

        Arguments:
        filename -- the name/path of the file that the new
        sound will be saved in as a string
        channels -- number of channels. Defaults to 1 (mono)
        sample_width -- sample width in bytes. Defaults to 2 (16-bit)
        sampling_rate -- samples per second. Defaults to 44100 (CD quality)
        """
        self.sound = wave.open(filename, 'wb')
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

    def combine_sample(self, index, value):
        self.samples[index] += value

    def __add__(self, other):
        size = min(len(self.samples), len(other.samples))
        for i in range(size):
            sample = self.samples[i] + other.samples[i]
            yield sample


class Tone(object):
    def __init__(self, note, amplitude, seconds):
        """Initialises the fields for Tone and its subclasses.
        Arguments:
        Note -- An integer representing the number of semitones away
        from the A above middle C
        Amplitude -- An integer defining the volume
        Seconds -- A float or integer defining how long the tone will be
        """
        self.note = note
        self.amplitude = amplitude
        self.seconds = seconds

    @property
    def frequency(self):
        return self.__frequency

    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, value):
        self.__note = value
        self.__frequency = self.__convert_note_to_freq(self.note)

    def __convert_note_to_freq(self, n):
        base_frequency = 440
        interval = 2.0**(1.0/12.0)
        note = base_frequency * interval**n
        return note

    def generate(self, sound):
        sample_number = int(sound.sampling_rate * self.seconds)
        for i in xrange(sample_number):
            sample = self._create_sample(sound.sampling_rate, i)
            sound.add_sample(sample)

    def _create_sample(self, sound, index):
        raise NotImplementedError


class SineTone(Tone):
    def _create_sample(self, sampling_rate, index):
        seconds_per_cycle = 1.0/self.frequency
        samples_per_cycle = seconds_per_cycle * sampling_rate
        cycle_size = 2 * math.pi
        sample = int((math.sin((index / samples_per_cycle) * cycle_size)) * self.amplitude)
        return sample


class SquareTone(Tone):
    def _create_sample(self, sampling_rate, index):
        seconds_per_cycle = 1.0/self.frequency
        samples_per_cycle = seconds_per_cycle * sampling_rate
        cycle_size = 2 * math.pi
        sinewave = math.sin(index / samples_per_cycle * cycle_size)
        if sinewave != 0:
            # Because a sign function doesn't exist in Python
            sample = int(self.amplitude * math.copysign(1, sinewave))
        else:
            sample = 0
        return sample


def test():
    sine_tone = SineTone(0, 2000, 0.5)
    square_tone = SquareTone(0, 2000, 0.5)
    upscale = Sound("up.wav")
    downscale = Sound("down.wav")

    for i in range(13):
        square_tone.note = i
        square_tone.generate(upscale)

    for i in range(0, -13, -1):
        sine_tone.note = i
        sine_tone.generate(downscale)

    scale = Sound("scale.wav")
    scale.samples = upscale + downscale
    upscale.save()
    downscale.save()
    scale.save()


test()
