def containsDuplicate(nums):
        hashset = set()
        for i in range(0, len(nums)):
            if nums[i] in hashset:
                return True
            else:
                hashset.add(nums[i])
        return False
print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
