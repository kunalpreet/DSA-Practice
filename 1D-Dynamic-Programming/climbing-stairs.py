def climbingStairs(n):
	if n <= 3:
		return 3
	n1, n2 = 2, 3
	for i in range(4, n + 1):
		a = n2
		n2 = n1 + n2
		n1 = a
	return n2


print(climbingStairs(3))
print(climbingStairs(5))
print(climbingStairs(4))
