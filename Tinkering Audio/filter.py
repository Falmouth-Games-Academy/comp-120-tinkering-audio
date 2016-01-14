"""Module for effects that can be applied to Sound objects"""

import math

class Effect():
    pass

class Filter(object):
    """Store methods and properties relating to filters.

    Note: I named most of the variables the same as in Audio EQ Cookbook
    (http://www.musicdsp.org/files/Audio-EQ-Cookbook.txt)
    as I don't know what a suitable name was since I don't know what they represent
    """

    def __init__(self, sound, center_frequency, bandwidth, gain):
        self.sampling_rate = sound.sampling_rate
        self.gain = gain
        self.center_frequency = center_frequency
        self.bandwidth = bandwidth
        self.memory = {'xmem1':0, 'xmem2':0, 'ymem1':0, 'ymem2':0}
        self.sample_number = 0

    @property
    def sampling_rate(self):
        return self.__sampling_rate

    @sampling_rate.setter
    def sampling_rate(self, value):
        self.__sampling_rate = value

    @property
    def gain(self):
        return self.__gain

    @gain.setter
    def gain(self, value):
        self.__gain = value

    @property
    def center_frequency(self):
        return self.__center_frequency

    @center_frequency.setter
    def center_frequency(self, value):
        self.__center_frequency = value

    @property
    def bandwidth(self):
        return self.__bandwidth

    @bandwidth.setter
    def bandwidth(self, value):
        self.__bandwidth = value

    @property
    def A(self):
        return 10 ** (self.gain/40)

    @property
    def w0(self):
        return 2 * math.pi * self.center_frequency / self.sampling_rate

    @property
    def w0_cosine(self):
        return math.cos(self.w0)

    @property
    def w0_sine(self):
        return math.sin(self.w0)

    @property
    def alpha(self):
        return self.w0_sine * math.sinh(math.log(2)/2 * self.bandwidth * self.w0 / self.w0_sine)

    # def __recalculate_intermediate_values(self):
    #     # Named these intermediate values the  same as in Audio EQ Cookbook
    #     # http://www.musicdsp.org/files/Audio-EQ-Cookbook.txt
    #     # as I don't know what a suitable name is since I don't know what they represent
    #     self.__A = 10 ** (self.gain/40)
    #     self.__w0 = 2 * math.pi * self.center_frequency / self.sampling_rate
    #     self.__w0_cosine = math.cos(self.w0)
    #     self.__w0_sine = math.sin(self.w0)
    #     self.__alpha = self.w0_sine * math.sinh(math.log(2)/2 * self.bandwidth * self.w0 / self.w0_sine)

    def _recalculate_coefficients(self):
        pass

    def process(self, orig_sample, sample_total, envelope=None):
        self._recalculate_coefficients()

        new_sample = int(self.b0 * orig_sample + self.b1 * self.memory['xmem1'] +
                      self.b2 * self.memory['xmem2'] - self.a1 * self.memory['ymem1'] -
                      self.a2 * self.memory['ymem2'])

        # if envelope != None:
        #      self.center_frequency = envelope.get_value(self.center_frequency, self.sample_number, sample_total)

        self.memory['xmem2'] = self.memory['xmem1']
        self.memory['xmem1'] = orig_sample
        self.memory['ymem2'] = self.memory['ymem1']
        self.memory['ymem1'] = new_sample

        self.sample_number += 1

        return new_sample

    def reset_memory(self):
        for key in self.memory.iterkeys():
            self.memory[key] = 0

class Peaking(Filter):
    def _recalculate_coefficients(self):
        self.a0 = 1 + self.alpha / self.A
        self.a1 = (-2 * self.w0_cosine) / self.a0
        self.a2 = (1 - self.alpha / self.A) / self.a0

        self.b0 = (1 + self.alpha * self.A) / self.a0
        self.b1 = (-2 * self.w0_cosine) / self.a0
        self.b2 = (1 - self.alpha * self.A) / self.a0

