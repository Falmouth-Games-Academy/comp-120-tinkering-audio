import wave
import struct

noise_out = wave.open('noise2.wav', 'w')
soundWave = wave.open('Roomba.wav', 'r')

# mode must be 'r', 'rb', 'w', or 'wb'

length = soundWave.getnframes()
frames = []

params = soundWave.getparams()
noise_out.setparams(params)

for i in xrange(length):
    wave_data = soundWave.readframes(1)
    data = struct.unpack("<h", wave_data)
    frames.append(int(data[0]))


def create_echo(sound_file, delay):
    values = []
    channels = 1
    s1 = sound_file
    s2 = sound_file[:]
    for index in range(delay, len(s1)):
        echo = 0.6*s2[index-delay]
        s1[index] += echo
        packaged_value = struct.pack("<h", s1[index])
        for j in xrange(channels):
            values.append(packaged_value)
    value_str = ''.join(values)
    noise_out.writeframes(value_str)
    noise_out.close()
    return values


def double(source):
    values = []
    channels = 2
    length = len(source) / 2 + 1
    target = [0] * length
    target_index = 0
    for source_index in range(0, length, 2):
        value = source[source_index]
        target[target_index] = value
        packaged_value = struct.pack("<h", target[target_index])
        target_index += 1
        for j in xrange(channels):
            values.append(packaged_value)
    value_str = ''.join(values)
    noise_out.writeframes(value_str)
    noise_out.close()
    return target


def half(source):
    values = []
    channels = 2
    length = len(source) * 2
    target = [0] * length
    source_index = 0
    for target_index in range(0, length):
        value = source[int(source_index)]
        target[target_index] = value
        packaged_value = struct.pack("<h", target[target_index])
        source_index += 0.5
        for j in xrange(channels):
            values.append(packaged_value)
    value_str = ''.join(values)
    noise_out.writeframes(value_str)
    noise_out.close()
    return target


def increase_volume(frames, length):
    """Doubles the volume"""
    for i in xrange(length):
        frames[i] *= 2


def highest_value():
    """finds the highest value"""
    maximum_number = 0
    for i in xrange(length):
        challenger = frames[i]
        if abs(challenger) > maximum_number:
            maximum_number = abs(challenger)
    return maximum_number


def count_sign_changes():
    """checks how many 0s"""
    numzero = 0
    for i in xrange(length):
        if frames[i] == 0:
            numzero += 1
    numzero /= 3    # 3 seconds
    numzero /= 2
    return numzero

#BitDepth = 2**15 - 1
#Volume = float(max()) / float(BitDepth)

create_echo(frames, 8000)

#double(frames)
#half(frames)
