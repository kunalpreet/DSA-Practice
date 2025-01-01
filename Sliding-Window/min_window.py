def minWindow(s, t):
	if len(t) > len(s):
		return ""

	window = {}
	ct = {}
	for c in t:
		ct[c] = 1 + ct.get(c, 0)

	res = [-1, -1]
	reslen = float("infinity")
	l = 0
	have = 0
	need = len(ct)
	for r in range(len(s)):
		c = s[r]
		window[c] = 1 + window.get(c, 0)

		if c in ct and window[c] == ct[c]:
			have += 1

		while have == need:
			winlength = r - l + 1
			if winlength < reslen:
				reslen = winlength
				res = [l, r]

			window[s[l]] -= 1
			if s[l] in ct and window[s[l]] < ct[s[l]]:
				have -= 1

			l += 1
	l, r = res
	if reslen == float("infinity"):
		return ""
	else:
		return s[l: r + 1]


print(minWindow(s="ADOBECODEBANC", t="ABC"))
print(minWindow(s="a", t="a"))
print(minWindow(s="a", t="aa"))
