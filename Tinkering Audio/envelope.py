"""Store classes relating to audio envelopes.

Classes:
Envelope -- has methods and fields for the application of an envelope
EnvelopePhase(Enum) -- enum to store which phase the envelope is in
EnvelopeType(Enum) -- enum to store the type of an envelope
"""

from enum import Enum

# Minimum threshold of human hearing
MIN_FREQUENCY = 20

class Envelope(object):

    """Contain fields and methods relating to audio envelopes.

    This class has fields and methods relating to both amplitude and
    frequency audio envelopes.

    Public Methods:
    get_value -- return the value of the amplitude or frequency after envelope has been applied
    """

    def __init__(self, type, sustain_level, attack_length, decay_length, sustain_length, release_length):
        """Initialise the fields.

        This method initialises the fields for the Envelope class. The sum of attack_length, decay_length,
        sustain_length and release_length must be 1.

        Arguments:
        type: the type of the envelope (frequency or amplitude) as an EnvelopeType
        sustain level: the sustain level. Absolute value for amplitude, difference in semitones for frequency
        attack_length: the length of the attack as a float representing the proportion of the sound
        decay_length: the length of the decay as a float representing the proportion of the sound
        sustain_length: the length of the sustain as a float representing the proportion of the sound
        release_length: the length of the release as a float representing the proportion of the sound
        """

        self.type = type
        self.attack_length = attack_length
        self.decay_length = decay_length
        self.sustain_level = sustain_level
        self.sustain_length = sustain_length
        self.release_length = release_length

    def get_value(self, default_value, sample_index, number_of_samples):
        """Return the appropriate amplitude or frequency value according to the envelope phase times.

        This method calculates the value that amplitude of frequency should take with the
        envelope applied to it.

        Arguments:
        default value -- the default amplitude or frequency of the tone
        sample_index -- the index of the sample the envelope will be applied to
        number_of_samples -- the total number of samples in the tone
        """

        phase = self.__get_envelope_phase(sample_index, number_of_samples)

        if phase == EnvelopePhase.attack:
            envelope = self.__get_attack(sample_index, number_of_samples)
            new_value = default_value * envelope
            if self.type == EnvelopeType.frequency and new_value < MIN_FREQUENCY:
                new_value = MIN_FREQUENCY

            return new_value

        if phase == EnvelopePhase.decay:
            envelope = self.__get_decay(sample_index, number_of_samples, default_value)
            new_value = default_value * envelope
            if self.type == EnvelopeType.frequency and new_value < MIN_FREQUENCY:
                new_value = MIN_FREQUENCY

            return new_value

        if phase == EnvelopePhase.sustain:
            new_value = self.__get_sustain(default_value)
            return new_value

        if phase == EnvelopePhase.release:
            envelope = self.__get_release(sample_index, number_of_samples)
            new_value = envelope * self.__get_sustain(default_value)
            if self.type == EnvelopeType.frequency and new_value < MIN_FREQUENCY:
                new_value = MIN_FREQUENCY

            return new_value

    def __get_attack(self, sample_index, number_of_samples):
        """Return the multiplier for the attack phase of the envelope

        This method calculates the multiplier that the amplitude or frequency
        should be multiplied in the attack phase of the envelope.
        It ensures that the value is gradually raised from 0 to its default
        level.
        It returns this value as a float.
        """

        attack_length = self.__get_attack_length(number_of_samples)
        envelope = float(sample_index / float(attack_length))
        return envelope

    def __get_decay(self, sample_index, number_of_samples, default_value):
        """Return the multiplier for the decay phase of the envelope.

        This method calculates the multiplier that the amplitude or frequency
        should be multiplied in the decay phase of the envelope. It ensures that
        it ends at the sustain level.
        It returns this value as a float.
        """

        decay_length = self.__get_decay_length(number_of_samples)
        decay_start = self.__get_attack_length(number_of_samples)
        decay_end = decay_start + decay_length
        sustain_level = self.__get_sustain(default_value)

        # Values worked out from solving simultaneous equations for line through 2 points
        m = (1.0 - (float(sustain_level) / default_value)) / (decay_start - decay_end)
        c = 1.0 - m * decay_start
        envelope = m * sample_index + c
        return envelope

    def __get_sustain(self, default_value):
        """Return the value for the sustain phase of the envelope.

        This method returns the absolute value to be used for the sustain phase
        of the envelope.
        """

        if self.type == EnvelopeType.amplitude:
            # If sustain level is entered as 0, sustain tone's default amplitude
            if self.sustain_level == 0:
                return default_value
            else:
                return self.sustain_level
        else:
            # Frequency sustain works relative to default frequency
            return self.__get_frequency_sustain_level(default_value)

    def __get_release(self, sample_index, number_of_samples):
        """Return the multiplier for the release phase of the envelope.

        This method calculates the multiplier that the amplitude or
        frequency should be multiplied for the release phase of the envelope.
        It will result in the volume or frequency tending towards 0.
        It returns this value as a float.
        """

        release_length = self.__get_release_length(number_of_samples)
        release_start = (self.__get_attack_length(number_of_samples) + self.__get_decay_length(number_of_samples) +
                          self.__get_sustain_length(number_of_samples))
        envelope = 1.0 - (float(sample_index - release_start) / float(release_length))
        return envelope

    def __get_attack_length(self, number_of_samples):
        """Return the length of the attack in samples"""
        return self.attack_length * number_of_samples

    def __get_decay_length(self, number_of_samples):
        """Return the length of the decay in samples"""
        return self.decay_length * number_of_samples

    def __get_sustain_length(self, number_of_samples):
        """Return the length of the sustain in samples"""
        return self.sustain_length * number_of_samples

    def __get_release_length(self, number_of_samples):
        """Return the length of the release in samples"""
        return self.release_length * number_of_samples

    def __get_frequency_sustain_level(self, default_frequency):
        # No semitone shift required if sustain level is 0
        if self.sustain_level == 0:
            return default_frequency
        else:
            # Used to calculate frequency increment between semitones
            INTERVAL = 2.0**(1.0/12.0)
            frequency = default_frequency * INTERVAL ** self.sustain_level
            return frequency

    def __get_envelope_phase(self, sample_index, number_of_samples):
        """Return the envelope phase of the given sample number"""
        attack_end = self.attack_length * number_of_samples
        decay_end = attack_end + self.decay_length * number_of_samples
        sustain_end = decay_end + self.sustain_length * number_of_samples
        release_end = sustain_end + self.release_length * number_of_samples

        if sample_index < attack_end:
            return EnvelopePhase.attack

        if sample_index < decay_end:
            return EnvelopePhase.decay

        if sample_index < sustain_end:
            return EnvelopePhase.sustain

        if sample_index < release_end:
            return EnvelopePhase.release


class EnvelopePhase(Enum):
    """Enum for different envelope phases"""
    # Arbitrary numbers for enum
    attack = 0
    decay = 1
    sustain = 2
    release = 3


class EnvelopeType(Enum):
    """Enum for different envelope types"""
    # Arbitrary numbers for enum
    amplitude = 0
    frequency = 1
