"""Module for tone classes. Tones can be seen as 'instruments'"""

import math

import sound
import envelope

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
        if self.amplitude_env != None:
            return self.amplitude_env.get_value(self.amplitude, sample_index, (self.seconds * sampling_rate))
        else:
            return self.amplitude

    def _get_frequency(self, sampling_rate, sample_index):
        if self.frequency_env != None:
            frequency = self.frequency_env.get_freq(self.frequency, sample_index, (self.seconds * sampling_rate))
            return frequency
        else:
            return self.frequency

    def __convert_note_to_freq(self, note):
        """Convert an integer note number to a frequency value.
        Return frequency as a float.
        """
        # The A above middle C
        BASE_FREQUENCY = 440
        INTERVAL = 2.0**(1.0/12.0)
        frequency = BASE_FREQUENCY * INTERVAL ** note
        return frequency

    def __convert_secs_to_samples(self, sound, seconds):
        """Convert seconds into sample numbers. Return number of samples
        as an int"""
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

    def get_sine_value(self, sampling_rate, sample_index, previous_phase):
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
        sine_value, phase = self.get_sine_value(sampling_rate, sample_index, previous_phase)
        sample = int(sine_value * amplitude)
        return sample, phase

# class SineTone(Tone):
#     def _create_sample(self, sampling_rate, sample_index, previous_value):
#         """Create a sample using a sine wave and returns it as an integer"""
#         frequency = self._get_frequency(sampling_rate, sample_index)
#         try:
#             seconds_per_cycle = 1.0/frequency
#         except ZeroDivisionError:
#             # Minimum threshold of human hearing
#             seconds_per_cycle = 1.0/20
#         samples_per_cycle = seconds_per_cycle * sampling_rate
#         cycle_size = 2 * math.pi
#         amplitude = self._get_amplitude(sampling_rate, sample_index)
#         increment_value = cycle_size / samples_per_cycle
#         sample = int((math.sin(previous_value + increment_value) * amplitude))
#         return sample, (previous_value + increment_value)
#
#
# class SquareTone(Tone):
#     def _create_sample(self, sampling_rate, sample_index):
#         """Create a sample using a square wave and returns it as an integer"""
#         frequency = self._get_frequency(sampling_rate, sample_index)
#         try:
#             seconds_per_cycle = 1.0/frequency
#         except ZeroDivisionError:
#             # Minimum threshold of human hearing
#             seconds_per_cycle = 1.0/20
#         samples_per_cycle = seconds_per_cycle * sampling_rate
#         cycle_size = 2 * math.pi
#         sinewave = math.sin(sample_index / samples_per_cycle * cycle_size)
#         amplitude = self._get_amplitude(sampling_rate, sample_index)
#         if sinewave != 0:
#             # Because a sign function doesn't exist in Python
#             sample = int(amplitude * math.copysign(1, sinewave) )
#         else:
#             sample = 0
#         return sample



class SquareTone(Tone):
    def _create_sample(self, sampling_rate, sample_index, previous_phase):
        """Create a sample using a square wave and returns it as an integer"""
        sine_value, phase = self.get_sine_value(sampling_rate, sample_index, previous_phase)
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
            sine_value, phase = self.get_sine_value(sampling_rate, sample_index, previous_phase)
            sample += int(sine_value * amplitude)
            frequency += self.frequency
        return sample, phase



    def __get_sine_sample(self, frequency, amplitude, sampling_rate, sample_index):
        """Return sine wave sample of given frequency and amplitude
        corresponding the current sample number.
        """
        seconds_per_cycle = 1.0/frequency
        samples_per_cycle = seconds_per_cycle * sampling_rate
        cycle_size = 2 * math.pi
        return int((math.sin((sample_index / samples_per_cycle) * cycle_size)) * amplitude)





#
#
# class HarmonicSawTone(Tone):
#     """Class that has methods to create a sawtooth tone through layering sine waves."""
#     def __init__(self, note, amplitude, seconds, levels, amplitude_env=None, frequency_env=None):
#         """Initialises the fields for the class. Takes one more argument than
#         the other Tone subclasses.
#         Arguments:
#         Note -- an integer representing the number of semitones away
#                 from the a above middle C
#         Amplitude -- an integer defining the volume
#         Seconds -- a float or integer defining how long the tone will be
#         Levels -- the number of harmonics
#         Envelope -- Envelope that will be applied to the tone's amplitude
#         """
#         super(HarmonicSawTone, self).__init__(note, amplitude, seconds, amplitude_env, frequency_env)
#         self.levels = levels
#
#     def _create_sample(self, sampling_rate, sample_index):
#         """Create a sawtooth wave sample using harmonic
#         sine waves and return it as an integer
#         """
#         sample = 0
#         frequency = self.frequency
#
#         # To levels + 1, as range stops before it. Start at 1 for calculations.
#         for i in xrange(1, self.levels + 1):
#             # Divide amplitude by harmonic number
#             amplitude = self._get_amplitude(sampling_rate, sample_index)
#             amplitude = float(amplitude) / i
#             sample += self.__get_sine_sample(frequency, amplitude, sampling_rate, sample_index)
#             frequency += self.frequency
#         return sample
#
#
#
#     def __get_sine_sample(self, frequency, amplitude, sampling_rate, sample_index):
#         """Return sine wave sample of given frequency and amplitude
#         corresponding the current sample number.
#         """
#         seconds_per_cycle = 1.0/frequency
#         samples_per_cycle = seconds_per_cycle * sampling_rate
#         cycle_size = 2 * math.pi
#         return int((math.sin((sample_index / samples_per_cycle) * cycle_size)) * amplitude)
