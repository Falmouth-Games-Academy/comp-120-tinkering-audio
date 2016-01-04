#function for splicing and swapping audio.

def spliceAndSwap():
  s1 = makeSound(pickAFile())                           
  s2 = makeEmptySoundBySeconds(10)                     #This creates a blank canvas
  targetIndex = 1
  for sourceIndex in range (20000, 40000):             #gets the sample values between the ranges
    value = getSampleValueAt(s1, sourceIndex)
    setSampleValueAt(s2, targetIndex, value)           #sets the value to the blank canvas
    targetIndex = targetIndex + 1                      #moves the target index
  for sourceIndex in range (70000, 80000):
    value = getSampleValueAt(s1, sourceIndex)
    setSampleValueAt(s2, targetIndex, value)
    targetIndex = targetIndex + 1
  for index in range(0, 10000):
    setSampleValueAt(s2, targetIndex, 0)               #creates blank sound after
    targetIndex = targetIndex + 1            
  explore(s2)
  return s2

 