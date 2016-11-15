import wave, struct

FILE = 'noise2.wav'
FILE_FORMAT = '<h'

noise = wave.open(FILE, 'r')
print noise.getparams()

print 'Length = ' + str(noise.getparams() [3] / noise.getparams()[2]) + 'secs'

noise_input =  noise.readframes(noise.getparams()[2])
noise_array = []

i = 0
while i  < len(noise_input):
   out = noise_input[i]
   for x in xrange(1, noise.getsampwidth()):
       out += noise_input[i+x]

   out = struct.unpack(FILE_FORMAT, out)[0]
   print out

   noise_array.append(int(out))

   i += noise.getsampwidth()

max_value = 0
for i in noise_array:
   if abs(i) > max_value:
       max_value = abs(i)

print 'Max Value in File = ' + str(max_value)

volume = round(float(max_value) / (2**(8 * noise.getsampwidth() - 1)), 2)

print 'Volume = ' +str(volume)

counter = 0
for i in noise_array:
   if i == 0:
       counter += 1
frequency = counter / 2

print 'Frequency = ' + str(frequency)