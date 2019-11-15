class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = 0
		self.storage = [None]*capacity

	def append(self, item):
		for i in range(0, self.capacity):
			if self.storage[i] is None:
				self.storage[i] = item
				return

	def get(self):
		self.storage.remove(None)
		print(self.storage)


r = RingBuffer(5)

r.append('a')
r.append('b')
r.append('c')
r.append('d')

# print(r.storage)
r.get()