def search(nums: list[int], target: int) -> int:
	l, r = 0, len(nums) - 1

	while l <= r:
		mid = l + (r - l) // 2
		if nums[mid] == target:
			return mid

		# left sorted portion
		if nums[l] <= nums[mid]:
			if target > nums[mid] or target < nums[l]:
				l = mid + 1
			else:
				r = mid - 1

		# right sorted portion
		else:
			if target < nums[mid] or target > nums[r]:
				r = mid - 1
			else:
				l = mid + 1
	return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([1, 3], 3))
