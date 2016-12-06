# Wave header
soundFile = wave.open('rubber_biscuit.wav', 'w')
soundFile.setframerate(44100)
soundFile.setnchannels(1)
soundFile.setnframes(44100)
soundFile.setcomptype('NONE', 'not compressed')
soundFile.setsampwidth(2)

NOTES = {
    "A":[],
    "E":[],
    "C":[],
    "D": []
}