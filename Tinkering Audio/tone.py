__author__ = 'Hat'

import math

import sound

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

    @frequency.setter
    def frequency(self, value):
        self.__frequency = value

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

    def __convert_secs_to_samples(self, sound, seconds):
        return int(sound.sampling_rate * seconds)

    def __generate(self, sound):
        """Generate samples using the same sampling rate as the
        supplied Sound object instance"""
        sample_number = self.__convert_secs_to_samples(sound, self.seconds)
        for i in xrange(sample_number):
            sample = self._create_sample(sound.sampling_rate, i)
            yield sample

    def add_tone(self, sound):
        """Add a tone to the given Sound object instance"""
        for sample in self.__generate(sound):
            sound.add_sample(sample)

    def layer_tone(self, sound, start_position):
        index = self.__convert_secs_to_samples(sound, start_position)
        for sample in self.__generate(sound):
            if index < len(sound.samples):
                sound.combine_sample(index, sample)
            else:
                return
            index += 1

    # def harmonise(self, sound, levels):
    #     initial_frequency = self.frequency
    #     for i in range(levels):
    #         for sample in self.generate(sound):
    #             sound.add_sample(sample)
    #         self.frequency += initial_frequency * i
    #     self.note = self.note

    def _create_sample(self, sound, index):
        raise NotImplementedError("Subclasses must implement _create_sample")


class SineTone(Tone):
    def _create_sample(self, sampling_rate, index):
        """Create a sample using a sine wave and returns it as an integer"""
        seconds_per_cycle = 1.0/self.frequency
        samples_per_cycle = seconds_per_cycle * sampling_rate
        cycle_size = 2 * math.pi
        sample = int((math.sin((index / samples_per_cycle) * cycle_size)) * self.amplitude)
        return sample


class SquareTone(Tone):
    def _create_sample(self, sampling_rate, index):
        """Create a sample using a square wave and returns it as an integer"""
        seconds_per_cycle = 1.0/self.frequency
        samples_per_cycle = seconds_per_cycle * sampling_rate
        cycle_size = 2 * math.pi
        sinewave = math.sin(index / samples_per_cycle * cycle_size)
        if sinewave != 0:
            # Because a sign function doesn't exist in Python
            sample = int(self.amplitude * math.copysign(1, sinewave) )
        else:
            sample = 0
        return sample