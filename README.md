# COMP120 Tinkering Audio

##Locations of Algorithms Required for Assignment

###Tone Generation
|Module|Class|Method(s)|
|---|---|---|
|tone|Tone|__generate|
|tone|SineTone, SquareTone, HarmonicSawTone|_create_sample|

###Tone Combination
|Module|Class|Method(s)|
|---|---|---|
|tone|Tone|combine_tone|
|sound|Sound|combine_sample, layer_sound_at_time, \__add__ (operator overload)|

###Audio Splice/Swap
|Module|Class|Method(s)|
|---|---|---|
|sound|Sound|insert_sound_at_time|

###Audio Envelopes/Echo
|Module|Class|Method(s)|
|---|---|---|
|sound|Sound|echo|
|envelope|Envelope|all|

###Parsing Tokens
|Module|Class|Method(s)|
|---|---|---|
|melody|Melody|all|

###Random Audio Generation
|Module|Class|Method(s)|
|---|---|---|
