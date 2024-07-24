# 주어진 연산 4개를 활용해 숫자를 1로 만들 수 있는 최소 횟수 구하기
class Solution:
    def num_to_one(self):
        X = int(input())

        cache = [0]*(X+1)
        
        for i in range(2, len(cache)):
            cache[i] = cache[i-1]+1      # 빼기

            if i % 5 == 0:
                cache[i] = min(cache[i], cache[i//5]+1)         # cache[i]: 현재 연산 횟수, cache[i//5]+1: i를 5로 나누는 경우 연산횟수
            if i % 3 == 0:
                cache[i] = min(cache[i], cache[i//3]+1)
            if i % 2 == 0:
                cache[i] = min(cache[i], cache[i//2]+1)

        print(cache[X])
    
s = Solution()
s.num_to_one()