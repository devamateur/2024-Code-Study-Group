class Solution:
    def make(self):
        # M을 만들 수 있는 높이의 최댓값 출력하기

        N, M = map(int, input().split())
        rice_cakes = list(map(int, input().split()))


        rice_cakes = sorted(rice_cakes)

        for h in range(min(rice_cakes), max(rice_cakes)):
            # 잘린 떡 리스트
            diff = [r-h if r > h else 0 for r in rice_cakes]           # 높이보다 작거나 같은 떡은 0이 됨
        
            left, right = 0, len(rice_cakes)-1
            diff_sum = 0              # 잘린 떡들의 합

            while left <= right:
                mid = (left + right)//2
                diff_sum += diff[mid]
                
                if diff_sum == M:
                    return h
                elif diff_sum < M:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

s = Solution()
print(s.make())