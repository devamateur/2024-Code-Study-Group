'''
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

[time] 30m
[문제] 주식 사고 파는 문제.
[풀이방식] :
- 투 포인터 방식, prev_price 변수로 이전 값 비교 트리거로 활용
    - while right < len(prices)를 진행하면 right가 맨 끝에 도달했을 때, right에 해당하는 값 계산을 못하는 경우가 발생함. (right+1 오류)
    - right-1 vs right로 비교 시, 결과를 저장한 맨 끝값과 비교를 해야할 때와 넘어가야할 때는 구분해야 함.
    - 이때, prev_price가 0이면 결과를 저장, prev_price에 값이 있으면 비교

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1 : return 0

        profit = [0]                    # 결과값 저장
        prev_price = 0                  # 이전값을 비교해야하는 경우 활용하는 변수
        left,right = 0,1                

        while right < len(prices) :

            if prices[right] > prices[right-1] :                
                if not prev_price :                             # prices[right] > prices[right-1], prev_price에 입력한 기록이 있으면
                    profit +=prices[right]-prices[left],
                    prev_price = profit[-1]
                else :                                          # profit의 마지막 값을 갱신
                    profit[-1] = prices[right]-prices[left]
                
                right +=1

            else :
                left = right
                right = left+1
                prev_price = 0                                  # 초기화

        return sum(profit)