class Solution:
    def install(self):
        # 일직선상 집의 위치가 주어질 때, 하나의 안테나만 설치해서 모든 집과의 거리가 최소가 되도록 하는 문제
        N = int(input())

        loc = list(map(int, input().split()))

        loc.sort()         # 집 위치 오름차순 정렬

        # 안테나를 가운데에 설치할 때 모든 집과의 거리가 최소가 됨
        print(loc[(N-1)//2])

s = Solution()
s.install()