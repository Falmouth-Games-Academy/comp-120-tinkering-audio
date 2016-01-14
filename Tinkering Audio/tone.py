"""Module for tone classes. Tones can be seen as 'instruments'"""

import math
import random

import sound
import envelope

MAX_AMPLITUDE = 32768

class Tone(object):

    """Contain methods for tone generation.

    This class contains fields and methods relating to tone generation.
    The tones are set up as if they were a particular instrument playing a
    particular note. Each instance of a Tone subclass has an associated note,
    amplitude and duration.
    This class should not be used directly, tones should be created through its
    subclasses.

    Public Methods:
    add_tone -- add the tone to a sound
    combine_tone -- layer the tone over a sound

    Public Fields and Properties:
    note -- the note of the tone
    amplitude -- the volume of the tone
    seconds -- the length of the tone
    amplitude_env -- the amplitude envelope to apply to the tone
    frequency_env -- the frequency envelope to apply to the tone
    """

    def __init__(self, note, amplitude, seconds, amplitude_env=None, frequency_env=None):
        """Initialise the fields for Tone and its subclasses.

        Arguments:
        note -- integer representing the number of semitones away from the A above middle C
        amplitude -- integer defining the volume
        seconds -- float or integer defining how long the tone will be
        amplitude_env -- the envelope that will be applied to the tone's amplitude as an envelope.Envelope
        frequency_env -- the envelope that will be applied to the tone's frequency as an envelope.Envelope
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

    def add_tone(self, sound):
        """Add a tone to the end of given Sound object instance"""
        for sample in self.__generate(sound):
            sound.add_sample(sample)

    def combine_tone(self, sound, start_position):
        """Combine the tone with a Sound object.

        This method combines the tone with a given sound object instance,
        starting at the given time. This can be used to add tones to a sound
        without having to create an  additional Sound object.
        If the tone is longer than the sound, it will extend past the end
        of the sound.

        Arguments:
        sound -- Sound object instance
        start_position -- start position in seconds
        """

        index = self.__convert_secs_to_samples(sound, start_position)
        for sample in self.__generate(sound):
            if index < len(sound.samples):
                sound.combine_sample(sample, index)
            else:
                sound.add_sample(sample)
            index += 1

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
        # Used to calculate frequency increment between semitones
        INTERVAL = 2.0**(1.0/12.0)
        frequency = BASE_FREQUENCY * INTERVAL ** note
        return frequency

    def __convert_secs_to_samples(self, sound, seconds):
        """Convert seconds into sample number and return as an integer."""
        return int(sound.sampling_rate * seconds)

    def __generate(self, sound):
        """Generate samples for the tone.

        This generator yields samples corresponding to the tones properties.
        The sound object the tone is being applied to is supplied to ensure
        that the matching sampling rate is used.
        """

        sample_number = self.__convert_secs_to_samples(sound, self.seconds)
        previous_phase = 0
        for i in xrange(sample_number):
            sample, previous_phase = self._create_sample(sound.sampling_rate, i, previous_phase)
            yield sample

    def _get_sine_value(self, sampling_rate, sample_index, previous_phase):
        """Return the sine value for the current phase and the previous phase.

        This method returns the value for the current phase of the sine wave corresponding
        to the sample number. It also returns the value of the phase of the sine wave
        for the previous sample.
        These values are returned as a tuple.

        Arguments:
        sampling_rate(int) -- the sampling rate of the sound
        sample_index(int) -- the position of the sample to be used in the calculation
        previous_phase(float) -- the previous phase, to be used in the calculation
        """

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

    def _create_sample(self, sound, index, value):
        raise NotImplementedError("Subclasses must implement _create_sample")


class SineTone(Tone):
    def _create_sample(self, sampling_rate, sample_index, previous_phase):
        """Return a sample value using a sine wave.

        This method creates a sample for a sine tone using a sine wave.
        It also returns the sine wave's phase as it is needed for correctly
        calculating the next sample.
        The sample value and sine wave phase are returned as a tuple.
        """

        amplitude = self._get_amplitude(sampling_rate, sample_index)
        sine_value, phase = self._get_sine_value(sampling_rate, sample_index, previous_phase)
        sample = int(sine_value * amplitude)
        return sample, phase


class SquareTone(Tone):
    def _create_sample(self, sampling_rate, sample_index, previous_phase):
        """Return a sample value using a square wave.

        This method creates a sample for a square tone based on the signs of
        a sine wave.
        It also returns the sine wave's phase as it is needed for correctly
        calculating the next sample.
        The sample value and sine wave phase are returned as a tuple.
        """

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
        """Initialises the fields for the class.

        This subclass of Tone takes an additional argument specifying how
        many harmonic levels will be used.

        Arguments:
        note -- an integer representing the number of semitones away
                from the a above middle C
        amplitude -- an integer defining the volume
        seconds -- a float or integer defining how long the tone will be
        levels -- the number of harmonics
        amplitude_env -- Envelope that will be applied to the tone's amplitude
        frequency_env -- Envelope that will be applied to the tone's frequency
        """

        super(HarmonicSawTone, self).__init__(note, amplitude, seconds, amplitude_env, frequency_env)
        self.levels = levels

    def _create_sample(self, sampling_rate, sample_index, previous_phase):
        """Return a sawtooth wave sample generated using harmonic sine waves.

        This method creates a sample for a sawtooth tone using combinations of
        harmonic sine waves.
        It also returns the sine wave's phase as it is needed for correctly
        calculating the next sample.
        The sample value and sine wave phase are returned as a tuple.
        """

        sample = 0
        frequency = self.frequency
        # To levels + 1, as range stops before it. Start at 1 so calculations are correct.
        for i in xrange(1, self.levels + 1):
            amplitude = self._get_amplitude(sampling_rate, sample_index)
            # Divide amplitude by harmonic number
            amplitude = float(amplitude) / i
            sine_value, phase = self._get_sine_value(sampling_rate, sample_index, previous_phase)
            sample += int(sine_value * amplitude)
            # Next harmonic
            frequency += self.frequency
        return sample, phase


class Noise(Tone):
    def __init__(self, note, amplitude, seconds, freq_filter=None, amplitude_env=None, frequency_env=None):
        super(Noise, self).__init__(note, amplitude, seconds, amplitude_env, frequency_env)
        self.freq_filter = freq_filter

    def _create_sample(self, sampling_rate, sample_index, previous_phase):
        """Return a random sample value to create white noise."""
        raw_sample = random.uniform(0, 1)
        amplitude = self._get_amplitude(sampling_rate, sample_index)
        sample = int(raw_sample * amplitude)
        sample_total = sampling_rate * self.seconds
        sample = self.freq_filter.process(sample, sample_total, self.frequency_env)
        return sample, None


    # def _create_sample(self, sampling_rate, sample_index, previous_phase):
    #     """Return a random sample value to create white noise."""
    #     raw_sample = random.uniform(0, 1)
    #     amplitude = self._get_amplitude(sampling_rate, sample_index)
    #     sample = int(raw_sample * amplitude)
    #     return sample, None