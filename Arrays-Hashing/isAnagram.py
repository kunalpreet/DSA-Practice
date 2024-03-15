def isAnagram(s, t):
	if len(s) != len(t):
		return False

	countS, countT = {}, {}
	for i in range(0, len(s)):
		countS[s[i]] = 1 + countS.get(s[i], 0)
		countT[t[i]] = 1 + countT.get(t[i], 0)
	for c in countS:
		if countS[c] != countT.get(c, 0):
			return False
	return True

print(isAnagram( "anagram", "nagaram"))
print(isAnagram( "kunal", "lanuk"))
print(isAnagram( "car", "rat"))

def k_elements(nums, k):
	if len(nums) == 1 and k == 1:
		return nums