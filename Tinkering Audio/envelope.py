
from enum import Enum

class Envelope(object):
    def __init__(self, attack_length, decay_length, sustain_level, sustain_length, release_length):
        self.attack_length = attack_length
        self.decay_length = decay_length
        self.sustain_level = sustain_level
        self.sustain_length = sustain_length
        self.release_length = release_length

    def get_value(self, default_amplitude, sample_index, number_of_samples):
        """Return the appropriate amplitude value according to the envelope  phase times
        Arguments:
        default_amplitude -- the default amplitude of the tone
        sample_index -- the index of the sample the envelope will be applied to
        number_of_samples -- the total number of samples in the tone"""
        attack_length = self.attack_length * number_of_samples
        decay_length = self.decay_length * number_of_samples
        sustain_length =  self.sustain_length * number_of_samples
        release_length =  self.release_length * number_of_samples

        decay_start = attack_length
        release_start = attack_length + decay_length + sustain_length

        phase = self.get_phase(sample_index, number_of_samples)

        if phase == EnvelopePhase.attack:
            envelope = float(sample_index / float(attack_length))
            amplitude = default_amplitude * envelope
            return amplitude

        if phase == EnvelopePhase.decay:
            envelope = 1.0 - (float(sample_index - decay_start) / float(decay_length))
            amplitude = default_amplitude * envelope
            if amplitude < self.sustain_level:
                return self.sustain_level
            else:
                return amplitude

        if phase == EnvelopePhase.sustain:
            amplitude = self.sustain_level
            return amplitude

        if phase == EnvelopePhase.release:
            envelope = 1.0 - (float(sample_index - release_start) / float(release_length))
            amplitude = envelope * self.sustain_level
            return amplitude

    def get_phase(self, sample_index, number_of_samples):
        """Return the phase of the given sample number"""
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
    attack = 0
    decay = 1
    sustain = 2
    release = 3
