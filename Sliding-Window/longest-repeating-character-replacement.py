def characterReplacement(s, k):
	count = 0
	maxS = ""
	res = s[0]
	for i in range(1, len(s)):
		if s[i] in res:
			res += s[i]
		elif count < k:
			res += s[0]
			count += 1
		else:
			if len(res) >= len(maxS):
				maxS = res
				res = s[i+1]
	if maxS == "":
		return res
	else:
		return maxS


print(characterReplacement("ABAA", 0))

