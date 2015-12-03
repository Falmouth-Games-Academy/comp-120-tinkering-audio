__author__ = 'Hat'

import sound

class Melody(object):
    def __init__(self, beats_per_minute, time_sig):
        """Intialise the fields.

        Arguments:

        beats -- the number of beats per minute (int)
        time_sig -- time signature as a string, e.g. '4/4'
        """
        self.beats_per_minute = beats_per_minute
        self.time_sig = time_sig

    @property
    def time_sig(self):
        return self.__time_sig

    @property
    def beats_per_bar(self):
        return self.__beats_per_bar

    @property
    def default_note(self):
        return self.__note_type

    @property
    def bar_length(self):
        return self.__bar_length

    @time_sig.setter
    def time_sig(self, sig):
        self.__time_sig = sig
        beats_per_bar, note_type = sig.split('/')
        self.__beats_per_bar = int(beats_per_bar)
        self.__note_type = int(note_type)
        self.__bar_length = self.beat_length * self.beats_per_bar

    @property
    def beat_length(self):
        return self.__beat_length

    @property
    def beats_per_minute(self):
        return self.__beats_per_minute
    @beats_per_minute.setter
    def beats_per_minute(self, value):
        self.__beats_per_minute = value
        self.__beat_length = 60.0 / self.beats_per_minute


    def parse_notes(self, note_string):
        """Parse the note string and return the note values and lengths

        Arguments:
        note_string -- string in the format notename:notetype, separated by spaces
        """
        notes = {'C': -9, 'D': -7, 'E': -5, 'F': -4, 'G': -2, 'A': 0, 'B': 2,
                 'c': 3, 'd': 5, 'e': 7, 'f':8, 'g': 10, 'a': 12, 'b': 14}
        note_values = []
        for note in note_string.split(' '):
            note_value, length = note.split(':')
            note_value = notes[note_value]
            note_length = self.bar_length / float(length)
            note_values.append((note_value, note_length))
        return note_values


    def create_melody(self, note_string, tone):
        """Create a melody from a string and return it as a Sound object

        Arguments:
        tone -- Tone object that the melody will be made from
        note_string --  string in the format notename:notetype, separated by spaces
        """
        melody = sound.Sound()
        note_values = self.parse_notes(note_string)
        print note_values
        for note in note_values:
            tone.note, tone.seconds = note
            tone.add_tone(melody)
        return melody
