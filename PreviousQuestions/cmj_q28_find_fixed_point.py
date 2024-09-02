class Solution:
    def binary_search(self):
        # 배열에서 고정점 찾기
        # 고정점: 인덱스와 원소가 같은 값인 경우 ex) a = [-15, -4, 2, 8, 13]에서 a[2] = 2이므로 고정점은 2
        N = int(input())

        numbers = list(map(int, input().split()))

        left, right = 0, N-1

        while left<=right:
            mid = (left + right)//2

            if numbers[mid] == mid:        # target이 mid 인덱스
                return mid
            elif numbers[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1
    
s = Solution()
print(s.binary_search())