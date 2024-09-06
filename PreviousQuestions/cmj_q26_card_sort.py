import heapq
class Solution:
    def card_sorting(self):
        N = int(input())

        cards = []

        for _ in range(N):
            cards.append(int(input()))
        
        # 번호순 오름차순 정렬
        cards.sort()

        # 우선순위 큐에 저장
        q = []

        for i in range(len(cards)):
            heapq.heappush(q, cards[i])    

        result = 0
        while len(q) >= 2:
            # 큐에서 2개씩 가져와서 합계를 구함
            a = heapq.heappop(q)
            b = heapq.heappop(q)
            sum_ = a + b
            # 합계를 다시 큐에 저장 -> 이 합계로 다른 번호와 또 합을 구함
            heapq.heappush(q, sum_)
            result += sum_     # 합계를 result에 저장

        print(result)
s = Solution()
s.card_sorting()