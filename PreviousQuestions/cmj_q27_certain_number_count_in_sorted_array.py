class Solution:
    def binary_search(self):
        # 정렬된 배열에서 x의 개수 구하기
        N, x = map(int, input().split())       # N: 배열 길이, x: 찾아야 하는 수

        numbers = list(map(int, input().split()))

        left, right = 0, len(numbers)-1

        # x를 포함하는 구간 first ~ last
        first, last = len(numbers)-1, 0

        # x가 등장하는 first 인덱스 구하기
        while left <= right:
            mid = (left + right)//2

            if numbers[mid] < x:
                left = mid + 1
            elif numbers[mid] > x:
                right = mid - 1
            else:                   # 찾은 경우
                first = min(first, mid)
                right = mid - 1

        left, right = 0, len(numbers)-1
        while left <= right:
            mid = (left + right)//2

            if numbers[mid] < x:
                left = mid + 1
            elif numbers[mid] > x:
                right = mid - 1
            else:                   # 찾은 경우
                last = max(last, mid)
                left = mid + 1

        # 구간 값이 바뀌지 않은 경우 -> x가 없는 것이므로 -1 리턴
        if first == len(numbers)-1 and last == 0:
            return -1
        # 구간이 있으면 해당 구간 길이 리턴
        return last-first+1
s = Solution()
print(s.binary_search())

'''
시간복잡도: O(N)

class Solution:
    def binary_search(self):
        # 정렬된 배열에서 x의 개수 구하기
        N, x = map(int, input().split())       # N: 배열 길이, x: 찾아야 하는 수

        numbers = list(map(int, input().split()))

        left, right = 0, len(numbers)-1
        count = 0

        while left <= right:
            mid = (left + right)//2

            if numbers[mid] < x:
                left = mid + 1
            elif numbers[mid] > x:
                right = mid - 1
            else:                   # 찾은 경우
                count += 1
                break
        
        if left >= right:          # 원소를 찾지 못한 경우 -1
            return -1

        # 원소를 찾은 경우, 해당 원소로 구성된 구간을 찾음
        while numbers[right] != x:               # right를 왼쪽으로 이동
            right -= 1

        while numbers[left] != x:                # left를 오른쪽으로 이동
            left += 1
        
        # 카운트를 해당 구간 길이로 갱신
        if numbers[left] == x and numbers[right] == x:
            count = right - left + 1

        return count
s = Solution()
print(s.binary_search())'''