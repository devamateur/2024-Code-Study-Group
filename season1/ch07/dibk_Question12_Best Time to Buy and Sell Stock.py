'''
prices = [7,1,5,0,3,6,4]

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ans = 0
        left,right = 0,1

        while right < len(prices):
            if prices[right]-prices[left] < 0:
                left = right
                right+=1
            else :
                max_ans = max(max_ans, prices[right]-prices[left])
                right+=1

        return max_ans


'''
solution :
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_value=prices[0]
        for i in prices:
            max_profit=max(max_profit,i-min_value)
            min_value=min(i,min_value)
        return max_profit

---

prices = [2,4,1]
Output : 0
Expected : 2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock = min(prices)
        min_idx = prices.index(min_stock)
        max_stock = max(prices[min_idx:])

        return max_stock-min_stock
        
'''