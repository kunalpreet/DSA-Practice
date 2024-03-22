def findMin(nums):
	l, r = 0, len(nums) - 1
	while l < r:
		mid = l + ((r - l) // 2)
		# search in right side
		if nums[mid] > nums[r]:
			l = mid + 1
		else:
			r = mid
	return nums[l]


print(findMin([1, 2]))
print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([1, 2, 3, 4, 5, 6, 7]))
print(findMin([11, 13, 15, 17]))
