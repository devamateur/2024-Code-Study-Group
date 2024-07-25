# 가로 길이 N, 세로 길이 2인 바닥을 채울 수 있는 모든 경우의 수 구하기
# 타일 종류: 2*1, 1*2, 2*2
class Solution:
    def make_tiles(self):
        N = int(input())

        cache = [0]*(N+1)
        cache[1] = 1
        cache[2] = 3
        for i in range(3, len(cache)):
            cache[i] = (cache[i-1]+cache[i-2]*2) % 796796
        print(cache[N])
    
s = Solution()
s.make_tiles()
