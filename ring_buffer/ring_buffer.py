# Queue Data Structure that uses a LinkedList
class RingBuffer:
  def __init__(self, capacity):
    # User-entered length of list
    self.capacity = capacity

    # points to the space in memory
    self.current = 0

    self.storage = [None]*capacity

  def __str__(self):
    return f'{self.storage}'

  def append(self, item):
    
    # if storage is all None -> this would allow us to assign the first element added as the curent oldest. But actually, we don't need to remove anything (using the current index which is already set to 0) until the array is at capacity. And if we are appending to the back of the array 

    # Replace the item at the index of the current_oldest with new item
    self.storage[self.current] = item

    # Move the current_oldest to the next in the array
    ## If at the end of the array, the current_oldest is at the beginning of the array
    if self.current == (len(self.storage) - 1):
      self.current = 0
    else:
      self.current += 1

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

# Original Idea

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = LinkedList()

  # Adds an item to the back of the array, like a normal append
  def append(self, item):
 
    # if the length of the array is less than the capacity / it's not full yet
    if len(self.storage) < self.capacity:
      self.storage.add_to_tail(item)
    
    # if the length of the array is equal to the capacity, we need to start removing items
    elif len(self.storage) >= self.capacity:
      # Remove the oldest item, which is at the head
      self.storage.remove_head()
      self.starage.add_to_tail(item)

^^ We keep track of 'old' items by ensuring they will always be at the head.

2 Problems:
  - In the starter code, `storage` is [None] * capacity, so the array will always hold 5 items, and I can't make the storage be of the LinkedList class
  - In the example outputs, the array must return the newest item replacing not only the oldest item, but also the same place that the oldest item was in. That makes no sense. How will I know the age of an item ??



"""