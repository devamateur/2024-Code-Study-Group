class Solution:
    def make_guild(self):
        N = int(input())

        # 멤버들의 공포도
        fear_rate = list(map(int, input().split()))

        fear_rate.sort()

        group_count = 0        # 현재 그룹에 포함된 멤버
        result = 0           # 그룹 수

        for i in range(len(fear_rate)):
            group_count += 1

            if group_count >= fear_rate[i]:
                result += 1
                group_count = 0
                
        print(result)

s = Solution()
s.make_guild()