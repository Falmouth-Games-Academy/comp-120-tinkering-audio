import wave, struct, math

from pygame.mixer_music import play

samprate = 44100

values = []
noise_a = wave.open('Orchestra.mp3', 'w')
noise_a.setnchannels(1)
noise_a.setsampwidth(2)
noise_a.setframerate(samprate)
noise_a.setnframes(44100 * 100)
noise_a.setcomptype('NONE', 'not compressed')
noise_a.getparams()
frequency = 500
delay = 0.1


#for i in range (0, 44100):
    #value = math.sin(2.0 * math.pi * frequency * (i / 44100.0)) * (0.5 * (2**15-1))
    #print value
    #data = struct.pack("<h", value)
    #frequency += 1
    #for j in range (0, 1):
        #values.append(data)


#print noise_a.getparams()


def echo (noise_a, delay):
    s1 = wave.open('Orchestra.mp3', 'r')
    s2 = wave.open('noise3.wav', 'w')
    for f in range (delay, s1.getsampwidth(s1)):
        echo = 0.6 * s1.getnchannels(s2, f - delay)
        combo = s1.getnchannels(s1, f) + echo
        s1.setnchannels(s1, f, combo)
        play(s1)
        return s1








#value_str = ''.join(values)
#noise_a.writeframes(value_str)
#noise_a.close()