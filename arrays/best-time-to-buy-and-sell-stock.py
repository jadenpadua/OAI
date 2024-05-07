class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPricePoint = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            # case where we find a new min point so update
            if prices[i] < minPricePoint:
                minPricePoint = prices[i]
            # this is the best you can get since you keep tabs on a minPricePoint
            currMinPricePointProfit = prices[i] - minPricePoint
            # update maxProfit if current min price point profit is better
            if currMinPricePointProfit > maxProfit:
                maxProfit = currMinPricePointProfit
        return maxProfit
