def twoSum(nums, target):
    l = len(nums)
    if l == 2:
        return [0, 1]
    count = {}
    for i in range(0, l):
        if nums[i] in count:
            return [i, count[nums[i]]]
        else:
            count[target - nums[i]] = i

print(twoSum([1, 2, 3, 4], 7))

def test():
    a = [1,2,3,4,5]

# returns the index positions of the variables