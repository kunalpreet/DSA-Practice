class Heap:
	def __init__(self):
		self.heap = [0]

	def push(self, val):
		self.heap.append(val)
		i = len(self.heap) - 1

		# Percolate up
		while i > 1 and self.heap[i] < self.heap[i // 2]:
			tmp = self.heap[i // 2]
			self.heap[i // 2] = self.heap[i]
			self.heap[i] = tmp
			i = i // 2

	def pop(self):
		if len(self.heap) == 1:
			return None
		if len(self.heap) == 2:
			return self.heap.pop()

		res = self.heap[1]

		self.heap[1] = self.heap.pop()
		i = 1
		# Percolate down
		while 2 * i < len(self.heap):
			if (2 * i + 1 < len(self.heap) and
					self.heap[2 * i + 1] < self.heap[2 * i] and
					self.heap[i] > self.heap[2 * i + 1]):
				tmp = self.heap[2 * i + 1]
				self.heap[2 * i + 1] = self.heap[i]
				self.heap[i] = tmp
				i = 2 * i + 1
			elif self.heap[i] > self.heap[2 * i]:
				tmp = self.heap[2 * i]
				self.heap[2 * i] = self.heap[i]
				self.heap[i] = tmp
				i = 2 * i
			else:
				break
		return res
