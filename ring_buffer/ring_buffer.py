class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = 0
		self.storage = [None]*capacity

	def append(self, item):
		for i in range(0, len(self.storage)):
			if self.storage[i] is None:
				# print('in if')
				self.storage[i] = item
				return

		if not None in self.storage:
			self.storage[self.current] = item
		
		self.current += 1

		if self.current is self.capacity:
			self.current = 0

	def get(self):
		new_list = [item for item in self.storage if item is not None]
		
		return new_list


# r = RingBuffer(5)

# r.append('a')
# r.append('b')
# r.append('c')
# r.append('d')
# r.append('e')
# # Past Capacity - should remove oldest (A)
# r.append('f') # get should return ['f', 'b', 'c', 'd', 'e']
# r.append('g') # get should return ['f', 'g', 'c', 'd', 'e']
# r.append('h') # get should return ['f', 'g', 'h', 'd', 'e']

# print(r.storage)
# print(r.get())