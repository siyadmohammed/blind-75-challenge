class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_price = 0
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
                max_price = price
            elif price > max_price:
                max_price = price
                profit = max(max_price - min_price, profit) 
        return profit