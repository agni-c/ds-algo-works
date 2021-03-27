class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float("inf")
        max_diff = 0
        for price in prices:
            if price < min_price:  min_price = price
            else:  max_diff = max(max_diff, price - min_price)
        return max_diff
            