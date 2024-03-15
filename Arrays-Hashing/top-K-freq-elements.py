def topKFrequent(nums, k):
    # inefficient time and space complexity
    # if len(nums) == 1 and k == 1:
    #     return nums
    # res = [0] * k
    # dict = {}
    # for i in nums:
    #     if i in dict:
    #         res = sorted(res, key=res.index, reverse=True)
    #         dict[i] += 1
    #         if dict[i] > res[k-1]:
    #             res[k-1] = i
    #     else:
    #         dict[i] = 1
    #         if dict[i] > res[k-1]:
    #             res[k-1] = i
    # return res
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    # better solution with O(n) complexity as you have to traverse through array twice
    # O(n) + O(n) = O(n)
    # same with space complexity O(n)


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1], 1))
print(topKFrequent([3, 3, 3, 3, 2, 2, 3, 3, 1, 1, 1, 5, 5, 5], 3))
