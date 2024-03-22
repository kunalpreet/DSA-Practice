def maxProfit(prices):
    profit, min = 0, prices[0]

    for p in prices[1:]:
        localProfit = p - min
        if p < min:
            min = p
        else:
            profit = max(localProfit, profit)
    return profit

# print(maxProfit([7,1,5,3,6,4]))
# print(maxProfit([7,6,4,3,1]))
