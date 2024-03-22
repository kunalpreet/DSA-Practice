def search(nums, target):
	l, r = 0, len(nums) - 1

	while l <= r:
		mid = l + ((r - l) // 2)
		if nums[mid] == target:
			return mid
		elif nums[mid] < target:
			l = mid + 1
		else:
			r = mid - 1
	return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))
