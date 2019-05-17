# Queue Data Structure that uses a LinkedList
class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def __str__(self):
    return f'{self.storage}'

  def append(self, item):
    self.storage.append(item)

  def get(self):
    # for each_item in self.storage:
        # if each_item is not None:
          # print(each_item)
    for each_item in self.storage:
      if each_item is not None:
        print(each_item)

new_ring = RingBuffer(5)
print(new_ring)
new_ring.append(4)
new_ring.append(3)
new_ring.append(2)
new_ring.append(1)
new_ring.get()
print(new_ring)


"""
PLAN

-> FIFO
  - Append()
    .. Adds an item to the back of the array, like a normal append

    # if the 
    if len(self.storage) < self.capacity:




"""