class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = 0
		self.storage = [None]*capacity

	def append(self, item):
		# if 
		for i in range(0, len(self.storage)):
			if self.storage[i] is None:
				self.storage[i] = item
				return
			# else:
			# 	print('in else')
				# self.storage[0] = item

	def get(self):
		new_list = [item for item in self.storage if item is not None]
		
		print(new_list, 'st')


r = RingBuffer(5)

r.append('a')
r.append('b')
r.append('c')
r.append('d')
r.append('e')
# Past Capacity - should remove oldest (A)
r.append('f') # get should return ['f', 'b', 'c', 'd', 'e']
# r.append('g') # get should return ['f', 'g', 'c', 'd', 'e']

# print(r.storage)
r.get() 