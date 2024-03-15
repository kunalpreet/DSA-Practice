#an anagram is when we sort a 2 strings and the same string is returned
# gat and tag are anagrams, if we sort both we get agt
# complexity is O(m * n), m = number of strs, n = average length of strings
from collections import defaultdict


def group_anagrams(strs):

    res = defaultdict(list)

    for str in strs:
        count = [0] * 26

        for c in str:
            count[ord(c) - ord("a")] += 1
            #The ord() function returns the number representing the unicode code of a specified character.
        res[tuple(count)].append(str)

    return res.values()

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))


