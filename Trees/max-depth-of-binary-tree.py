from collections import deque


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		if not root:
			return 0

		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

	# ITERATIVE DFS
	def maxDepthITERATIVE_DFS(self, root: TreeNode) -> int:
		stack = [[root, 1]]
		res = 0

		while stack:
			node, depth = stack.pop()

			if node:
				res = max(res, depth)
				stack.append([node.left, depth + 1])
				stack.append([node.right, depth + 1])
		return res

	# BFS
	def maxDepth_BFS(self, root: TreeNode) -> int:
		q = deque()
		if root:
			q.append(root)

		level = 0

		while q:

			for i in range(len(q)):
				node = q.popleft()
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			level += 1
		return level
