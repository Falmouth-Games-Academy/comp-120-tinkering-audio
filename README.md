# COMP120 Tinkering Audio

Running main.py will execute functions that use the algorithms implemented for the assignment to create the following sounds for the Kivy game:

|Sound|Filename|
|---|---|
|Title music|title.wav|
|Level start sound|jingle.wav|
|Pellet eating sound|chomp_high.wav and chomp_low.wav|
|Power-up sound|power_up.wav|
|Frightened enemy sound|frightened.wav|
|Retreating enemy sound|retreat.wav|
|Player death sound|death.wav|
|Game over sound | game_over.wav|

The sounds can be found in the output folder.

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
|sound|Sound|append_sound (when combined with other things)|
|sound|Sound|reverse|

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
