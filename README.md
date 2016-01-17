# COMP120 Tinkering Audio

This algorithms implemented for the assignment are used in this program to create the following sounds for the Kivy game:
* Title music
* Level start sound
* Pellet eating sound
* Power-up sound
* Frightened enemy sound
* Retreating enemy sound
* Player death sound


##Additional Libraries Used
[enum34](https://pypi.python.org/pypi/enum34)

##Locations of Methods Relating to Algorithms Required for Assignment

###Tone Generation
|Module|Class|Method(s)|
|---|---|---|
|tone|Tone|create_tone, __generate|
|tone|SineTone, SquareTone, HarmonicSawTone|_create_sample|

###Tone Combination
|Module|Class|Method(s)|
|---|---|---|
|tone|Tone|combine_tone|
|sound|Sound|combine_sample_at_index, layer_sound_at_time, \__add__ (operator overload)|

###Audio Splice/Swap
|Module|Class|Method(s)|
|---|---|---|
|sound|Sound|insert_sound_at_time|

###Audio Envelopes/Echo
|Module|Class|Method(s)|
|---|---|---|
|sound|Sound|echo, feedback_echo|
|envelope|Envelope|all|

###Parsing Tokens
|Module|Class|Method(s)|
|---|---|---|
|melody|Melody|all|

###Random Audio Generation
|Module|Class|Method(s)|
|---|---|---|
|melody|Melody|create_shuffled_melody|
|tone|Noise|_create_sample|
