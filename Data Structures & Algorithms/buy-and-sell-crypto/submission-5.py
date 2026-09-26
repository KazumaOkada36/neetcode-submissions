class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        difference = 0
        while r < len(prices):
            differencey = prices[r]-prices[l]
            difference = max(differencey, difference)
            if prices[r]<prices[l]:
                l = r
                r += 1
            else:
                r+= 1


        return difference
