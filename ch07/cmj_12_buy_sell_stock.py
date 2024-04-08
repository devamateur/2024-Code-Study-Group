class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        min_price = prices[0]
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i]-min_price)
            
        return profit

    # 이 문제는 굳이 dp로 해결하면 시간이 더 오래걸려서 큰 의미는 없지만..
    def dp(self, prices: List[int]) -> int:
        profit = [0]*len(prices)           # 날짜별 최대 수익을 저장하는 캐시

        min_price = prices[0]

        for i in range(1, len(prices)):       # 1부터 시작, 첫번째 날 얻는 수익(profit[0])은 0이므로
            min_price = min(min_price, prices[i])
            profit[i] = max(profit[i-1], prices[i] - min_price)         # profit[i-1]: i-1일까지 얻는 최대 수익
            
        return profit[-1]
    
''' 시간초과
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
    
        for i in range(len(prices)):
            min_price = min(prices[:i+1])
            if i > prices.index(min_price):
                profit = max(profit, prices[i] - min_price)
'''