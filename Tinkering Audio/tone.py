"""Module for tone classes. Tones can be seen as 'instruments'"""

import math
import random

import sound
import envelope

MAX_AMPLITUDE = 32768

class Tone(object):
    def __init__(self, note, amplitude, seconds, amplitude_env=None, frequency_env=None):
        """Initialises the fields for Tone and its subclasses.
        Arguments:
        Note -- An integer representing the number of semitones away
        from the A above middle C
        Amplitude -- An integer defining the volume
        Seconds -- A float or integer defining how long the tone will be
        Envelope -- Envelope that will be applied to the tone's amplitude
        """
        self.note = note
        self.amplitude = amplitude
        self.seconds = seconds
        self.amplitude_env = amplitude_env
        self.frequency_env = frequency_env

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

    def _get_amplitude(self, sampling_rate, sample_index):
        """Return the amplitude after any envelopes have been applied to it.

        This method returns the amplitude for a specific sample
        after any envelopes have been applied to it.

        Arguments:
        sampling_rate -- the sampling rate of the sound as an integer
        sample_index -- the index of the sample that the amplitude should be retrieved
        """

        if self.amplitude_env != None:
            return self.amplitude_env.get_value(self.amplitude, sample_index, (self.seconds * sampling_rate))
        else:
            return self.amplitude

    def _get_frequency(self, sampling_rate, sample_index):
        """Return the frequency after any envelopes have been applied to it.

        This method returns the frequency for a specific sample
        after any envelopes have been applied to it.

        Arguments:
        sampling_rate -- the sampling rate of the sound as an integer
        sample_index -- the index of the sample that the frequency should be retrieved
        """
        if self.frequency_env != None:
            frequency = self.frequency_env.get_value(self.frequency, sample_index, (self.seconds * sampling_rate))
            return frequency
        else:
            return self.frequency

    def __convert_note_to_freq(self, note):
        """Convert an integer note number to a frequency value and return it.

        This method converts an integer note value to a frequency value. The A
        above middle C is 0, and each integer above or below is a semitone above
        or below respectively. Floats can be used to represent intervals smaller
        than a semitone. Frequency is returned as a float.

        Arguments:
        note -- the note number to convert to a frequency
        """

        # The A above middle C
        BASE_FREQUENCY = 440
        INTERVAL = 2.0**(1.0/12.0)
        frequency = BASE_FREQUENCY * INTERVAL ** note
        return frequency

    def __convert_secs_to_samples(self, sound, seconds):
        """Convert seconds into sample number and return as an integer."""
        return int(sound.sampling_rate * seconds)

    def __generate(self, sound):
        """Generate samples using the same sampling rate as the
        supplied Sound object instance"""
        sample_number = self.__convert_secs_to_samples(sound, self.seconds)
        previous_value = 0
        for i in xrange(sample_number):
            sample, previous_value = self._create_sample(sound.sampling_rate, i, previous_value)
            yield sample

    def add_tone(self, sound):
        """Add a tone to the end of given Sound object instance"""
        for sample in self.__generate(sound):
            sound.add_sample(sample)

    def combine_tone(self, sound, start_position):
        """Combine the tone with the given Sound object instance,
        starting at the given time.

        Arguments:
        sound -- Sound object instance
        start_position -- start position in seconds
        """
        index = self.__convert_secs_to_samples(sound, start_position)
        for sample in self.__generate(sound):
            if index < len(sound.samples):
                sound.combine_sample(index, sample)
            else:
                sound.add_sample(sample)
            index += 1

    # This function doesn't really work in a sensible way, as I
    # was using it for testing. But I decided to leave it in
    # because it creates some interesting sounds
    def harmonise(self, sound, levels):
        """Add harmonic frequencies to the tone and layer
        the result on the beginning of the sound"""
        fundamental_frequency = self.frequency
        initial_amplitude = self.amplitude
        for i in xrange(1, levels + 1):
            index = 0
            self.amplitude = float(initial_amplitude) / i
            for sample in self.__generate(sound):
                sound.combine_sample(index, sample)
                index += 1
            self.frequency += fundamental_frequency
        # Ensure frequency is reset to match the note on finish
        self.note = self.note

    def _create_sample(self, sound, index, value):
        raise NotImplementedError("Subclasses must implement _create_sample")

    def _get_sine_value(self, sampling_rate, sample_index, previous_phase):
        """Return the sine value for the current phase and the current phase

        Arguments:
        sampling_rate(int) -- the sampling rate of the sound
        sample_index(int) -- the position of the sample to be used in the calculation
        previous_phase(float) -- the previous phase, to be used in the calculation"""
        frequency = self._get_frequency(sampling_rate, sample_index)
        try:
            seconds_per_cycle = 1.0/frequency
        except ZeroDivisionError:
            # Minimum threshold of human hearing
            seconds_per_cycle = 1.0/20
        samples_per_cycle = seconds_per_cycle * sampling_rate
        cycle_size = 2.0 * math.pi
        phase_increment = cycle_size / samples_per_cycle
        phase = previous_phase + phase_increment
        sine_value = math.sin(phase)
        return sine_value, phase


class SineTone(Tone):
    def _create_sample(self, sampling_rate, sample_index, previous_phase):
        """Create a sample using a sine wave and returns it as an integer"""
        amplitude = self._get_amplitude(sampling_rate, sample_index)
        sine_value, phase = self._get_sine_value(sampling_rate, sample_index, previous_phase)
        sample = int(sine_value * amplitude)
        return sample, phase


class SquareTone(Tone):
    def _create_sample(self, sampling_rate, sample_index, previous_phase):
        """Create a sample using a square wave and returns it as an integer"""
        sine_value, phase = self._get_sine_value(sampling_rate, sample_index, previous_phase)
        amplitude = self._get_amplitude(sampling_rate, sample_index)
        if sine_value != 0:
            # Because a sign function doesn't exist in Python
            sample = int(amplitude * math.copysign(1, sine_value) )
        else:
            sample = 0
        return sample, phase


class HarmonicSawTone(Tone):
    """Class that has methods to create a sawtooth tone through layering sine waves."""
    def __init__(self, note, amplitude, seconds, levels, amplitude_env=None, frequency_env=None):
        """Initialises the fields for the class. Takes one more argument than
        the other Tone subclasses.
        Arguments:
        Note -- an integer representing the number of semitones away
                from the a above middle C
        Amplitude -- an integer defining the volume
        Seconds -- a float or integer defining how long the tone will be
        Levels -- the number of harmonics
        Envelope -- Envelope that will be applied to the tone's amplitude
        """
        super(HarmonicSawTone, self).__init__(note, amplitude, seconds, amplitude_env, frequency_env)
        self.levels = levels

    def _create_sample(self, sampling_rate, sample_index, previous_phase):
        """Create a sawtooth wave sample using harmonic
        sine waves and return it as an integer
        """
        sample = 0
        frequency = self.frequency
        # To levels + 1, as range stops before it. Start at 1 for calculations.
        for i in xrange(1, self.levels + 1):
            # Divide amplitude by harmonic number
            amplitude = self._get_amplitude(sampling_rate, sample_index)
            amplitude = float(amplitude) / i
            sine_value, phase = self._get_sine_value(sampling_rate, sample_index, previous_phase)
            sample += int(sine_value * amplitude)
            frequency += self.frequency
        return sample, phase

class Noise(Tone):
    def _create_sample(self, sampling_rate, sample_index, previous_phase):
        return random.randrange(MAX_AMPLITUDE), None