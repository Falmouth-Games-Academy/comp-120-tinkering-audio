# COMP120 Tinkering Audio

The program is currently able to generate a sine tone and a square tone and combine them.
I intend to change how the Sound class and Tone classes work so that it is more flexible and able to combine and add tones without creating new Sound object instances.

May restructure it so that the tones are associated with a specific Sound instance and the frequency, amplitude, etc are passed in as arguments to the methods in Tone. In the real world I guess this would be like the tones are 'instruments' that are used in the sound.
