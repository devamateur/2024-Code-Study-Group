class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy = prices[0]       # 주식을 사는 날

        for i in range(1, len(prices)):
            # 더 작은 값이 나오면 그 값으로 갱신
            if buy > prices[i]:
                buy = prices[i]

            # 이득이 생기면 팔기
            if prices[i] - buy > 0:
                profit += prices[i]-buy
                buy = prices[i]          # 사는 날 갱신
        return profit