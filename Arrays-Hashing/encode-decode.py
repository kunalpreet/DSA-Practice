def encode(strs):
	res = ""
	for s in strs:
		res = res + str(len(s)) + "#" + s
	return res


def decode(s):
	res, i = [], 0

	while i < len(s):
		j = i
		while s[j] != "#":
			j += 1
		length = int(s[i:j])
		res.append(s[j + 1:j + 1 + length])
		i = j + 1 + length
	return res


print(decode(encode(["lint", "code", "love", "you"])))
print(decode(encode(["we", "say", ":", "yes"])))
