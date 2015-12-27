#function for splicing and swapping audio.

def spliceAndSwap():
  source = makeSound(pickAFile())
  target = makeEmptySoundBySeconds(10)
  targetIndex = 1
  for sourceIndex in range (40000, 60000):
    value = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target, targetIndex, value)
    targetIndex = targetIndex + 1
  for sourceIndex in range (70000, 80000):
    value = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target, targetIndex, value)
    targetIndex = targetIndex + 1
  for index in range(0, 10000):
    setSampleValueAt(target, targetIndex, 0)
    targetIndex = targetIndex + 1        
    explore(target)
    return target

 