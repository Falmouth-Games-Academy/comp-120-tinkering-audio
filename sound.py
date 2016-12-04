import wave, struct, math

samprate = 44100

values = []
noise_a = wave.open('noise3.wav', 'w')
noise_a.setnchannels(1)
noise_a.setsampwidth(2)
noise_a.setframerate(samprate)
noise_a.setnframes(44100 * 100)
noise_a.setcomptype('NONE', 'not compressed')
noise_a.getparams()
frequency = 500

for i in range (0, 44100):
    value = math.sin(2.0 * math.pi * frequency * (i / 44100.0)) * (0.5 * (2**15-1))
    print value
    data = struct.pack("<h", value)
    frequency += 4
    for j in xrange (0, 1):
        values.append(data)

value_str = ''.join(values)
noise_a.writeframes(value_str)
noise_a.close()
