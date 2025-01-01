# from collections import deque
#
#
# def bfs(graph, node):
# 	visited = set()
# 	queue = deque()
#
# 	visited.add(node)
# 	queue.append(node)
#
# 	while queue:
# 		s = queue.popleft()
# 		print(s, end=" ")
#
# 		for n in graph[s]:
# 			if n not in visited:
# 				visited.add(n)
# 				queue.append(n)
#
#
# graph = {
# 	'A': ['B', 'C'],
# 	'B': ['D', 'E', 'F'],
# 	'C': ['G'],
# 	'D': [],
# 	'E': [],
# 	'F': ['H'],
# 	'G': ['I'],
# 	'H': [],
# 	'I': []
# }
#
# bfs(graph, 'A')

from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def bfs(root):
	queue = deque()

	if root:
		queue.append(root)

	level = 0
	while len(queue) > 0:
		print("level: ", level)
		for i in range(len(queue)):
			curr = queue.popleft()
			print(curr.val)
			if curr.left:
				queue.append(curr.left)
			if curr.right:
				queue.append(curr.right)
		level += 1
