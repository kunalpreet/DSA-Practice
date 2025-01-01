from typing import List


def knapsack(profit: List[int], weight: List[int], capacity: int) -> int:
	n = len(profit)
	m = capacity

	dp = [0] * (m + 1)

	for c in range(m + 1):
		if weight[0] <= c:
			dp[c] = profit[0]
	print(dp)

	for i in range(1, n):
		currow = [0] * (m + 1)
		for c in range(m + 1):
			skip = dp[c]
			include = 0
			if c - weight[i] >= 0:
				include = profit[i] + dp[c - weight[i]]
			currow[c] = max(skip, include)
		dp = currow
		print(dp)
	return dp[capacity]


profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
capacity = 8
knapsack(profit, weight, capacity)
