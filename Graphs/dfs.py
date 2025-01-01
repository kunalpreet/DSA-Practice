from collections import deque


def dfs(graph, node):
	visited = set()
	stack = deque()

	visited.add(node)
	stack.append(node)

	while stack:
		s = stack.pop()
		print(s, end=" ")

		for n in reversed(graph[s]):
			if n not in visited:
				visited.add(n)
				stack.append(n)


graph = {
	'A': ['B', 'G'],
	'B': ['C', 'D', 'E'],
	'C': [],
	'D': [],
	'E': ['F'],
	'F': [],
	'G': ['H'],
	'H': ['I'],
	'I': [],
}

dfs(graph, 'A')
