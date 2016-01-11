"""This module includes a class for creating melodies from strings"""

import random
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
    def default_note_type(self):
        return self.__default_note_type

    @property
    def bar_length(self):
        return self.__bar_length

    @time_sig.setter
    def time_sig(self, time_sig):
        """Set the time signature and related properties.

        Set up the time signature and related properties including beats
        per bar, default note type, and the length of the bar (in seconds).
        Default note type is given in terms of musical value, derived from the
        time signature, e.g. a crotchet is 4, a quaver is 8.
        Beats per bar is the number of this note type in a bar, similarly derived
        from the time signature.

        Arguments:
        time_sig -- time signature as a string, e.g. '4/4'
        """

        self.__time_sig = time_sig
        beats_per_bar, default_note_type = time_sig.split('/')
        self.__beats_per_bar = int(beats_per_bar)
        self.__default_note_type = int(default_note_type)
        self.__bar_length = self.beat_length * self.beats_per_bar

    @property
    def beat_length(self):
        return self.__beat_length

    @property
    def beats_per_minute(self):
        return self.__beats_per_minute

    @beats_per_minute.setter
    def beats_per_minute(self, value):
        """Set the beats per minute and beat length.

        Set the beats per minute property and the beat length in seconds.
        The beat length will consequently be the length of the default note type.
        """

        self.__beats_per_minute = value
        self.__beat_length = 60.0 / self.beats_per_minute

    def create_melody(self, note_string, tone):
        """Create a melody from a string and return it as a Sound object

        This method creates a melody from a string and returns it as a
        Sound object. The notes in the string should be in the form
        notename:octave:notetype and each note should be separated by a space.
        The Tone object used for the melody can be seen as the 'instrument'.

        Arguments:
        tone -- Tone object that the melody will be made from
        note_string --  string in the format notename:octave:notetype, separated by spaces
        """

        melody = sound.Sound()
        note_values = self.__parse_notes(note_string)
        print note_values
        for note in note_values:
            tone.note, tone.seconds = note
            tone.add_tone(melody)
        return melody

    def create_shuffled_melody(self, note_string, tone):
        """Shuffle a string to create a random melody and return it as a Sound object.

        This method shuffles a string of notes and created a melody which is returned as a
        Sound object. The notes in the string should be in the form
        notename:octave:notetype and each note should be separated by a space.
        The Tone object used for the melody can be seen as the 'instrument'.

        Arguments:
        tone -- Tone object that the melody will be made from
        note_string --  string to be shuffled in the format notename:octave:notetype, separated by spaces
        """

        note_list = note_string.split()
        random.shuffle(note_list)
        shuffled_note_string = ' '.join(note_list)
        return self.create_melody(shuffled_note_string, tone)

    def get_time_at_beat(self, beat_number):
        """Return the time in seconds of a given beat."""
        return self.bar_length / self.default_note_type * beat_number

    def __parse_notes(self, note_string):
        """Parse the note string and return the note values and lengths.

        This method parses a string of notes given in the form
        notename:octave:notetype, separated by spaces into numbers to be
        used for frequency conversion. Octave number 4 is middle C.
        This method returns a list of tuples containing the note value and note
        length.

        Arguments:
        note_string -- string in the format notename:octave:notetype, separated by spaces.
        """

        BASE_OCTAVE = 4
        NOTES_IN_OCTAVE = 12
        notes = {'C': -9, 'C#': -8, 'Db': -8, 'D': -7, 'D#': -6, 'Eb': -6,
                 'E': -5, 'F': -4, 'F#': -3, 'Gb': -3, 'G': -2, 'G#': -1,
                 'Ab': -1, 'A': 0, 'A#': 1, 'Bb': 1, 'B': 2}
        note_values = []

        for note in note_string.split(' '):
            note_value, octave, length = note.split(':')
            octave_shift = NOTES_IN_OCTAVE * (int(octave) - BASE_OCTAVE)
            note_value = notes[note_value] + octave_shift
            note_length = self.bar_length / float(length)
            note_values.append((note_value, note_length))
        return note_values




