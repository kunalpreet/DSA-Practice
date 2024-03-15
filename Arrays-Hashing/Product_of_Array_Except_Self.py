def productExceptSelf(nums):
	res = [1] * len(nums)
	for i in range(1, len(nums)):
		res[i] = res[i-1] * nums[i-1]
	
	postfix = 1
	for i in range(len(nums)-1, -1, -1):
		res[i] = postfix * res[i]
		postfix = postfix * nums[i]
	return res

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
