# N가지 화폐를 이용해 M원을 만드는 문제
# 이 때 화폐 개수를 최소로 사용해야 함
class Solution:
    def return_count(self):
        # N: 화폐 개수
        # M: 만들어야 하는 돈(원)
        N, M = map(int, input().split())

        money = []
        for i in range(N):
            money.append(int(input()))

        d = [10001] * (M+1)       # M의 최댓값으로 초기화

        d[0] = 0
        for i in range(N):      # 모든 화폐 단위에 대해
            for j in range(money[i], M + 1):              # M원을 만드는 데 필요한 최소 화폐 개수 개산
                d[j] = min(d[j], d[j-money[i]] + 1)

        print(d[M]) if d[M] != 10001 else print(-1)

s=Solution()
s.return_count()