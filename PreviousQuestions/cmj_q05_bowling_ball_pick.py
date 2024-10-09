from itertools import combinations
class Solution:
    def pick(self):
        '''
            두 사람이 무게가 다른 볼링공을 고르는 경우의 수 구하기
        '''
        # N: 볼링공 개수, M: 볼링공 무게 (1~M)
        N, M = map(int, input().split())

        weights = list(map(int, input().split()))

        # 두 사람이 무게가 다른 볼링공 2개를 고르는 경우의 수 = N개 볼링공에서 2개를 고르는 경우 - 무게가 같은 볼링공을 고르는 경우의 수
        comb = list(combinations(weights, 2))

        dup_count = 0
        for a, b in comb:
            if a == b:
                dup_count += 1        # 무게가 같은 볼링공 개수 카운트

        print(len(comb) - dup_count)

s = Solution()
s.pick()