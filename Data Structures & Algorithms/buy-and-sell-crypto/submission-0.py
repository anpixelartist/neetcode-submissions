class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0 
        profit = 0
        while i < len(prices)-1:
            j = i+1

            while j < len(prices):
                if prices[j]-prices[i]>profit:
                    profit = prices[j]-prices[i]
                    j +=1
                else:
                    j+= 1
            i+= 1    
        return profit
            
        