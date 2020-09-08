'''Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.'''

import sys

#sol1. sys.maxsize
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set variable
        profit = 0
        # infinite to min_price -> replaced immediately or in any price
        min_price = sys.maxsize
        
        # compare element
        for price in prices:
            # min (current price, set min_price)
            min_price = min(price, min_price)
            # max (current profit, current price - min_price)
            profit = max(profit, price - min_price)
            
        return profit