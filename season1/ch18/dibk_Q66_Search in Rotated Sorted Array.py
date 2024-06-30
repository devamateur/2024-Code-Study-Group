'''
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

[time] failed
[문제] nums리스트는 특정 위치에서 부터 오름차순으로 정렬되어 있다. 여기서 이진 탐색 알고리즘으로 target값을 찾기.
[풀이방식] :
- 문제 이해하는 데 시간이 걸림(Q65과 차이가 있음)
- 우선 k의 위치(최소값의 위치)를 구하고, k위치의 값과 target값을 비교해서 찾기
    - 

'''
# solution
# ex)
## nums = [4,5,6,7,8,1,2,3]
## target = 8
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums: return -1

        # k의 위치(최소값 위치)를 피벗으로 설정
        left, right = 0, len(nums) - 1
        
        while left < right:
            # mid = left + (right - left) // 2
            mid = (right + left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        # 최소값의 위치
        pivot = left            # pivot : 5-idx
        
        # 피벗 기준으로 이진 검색
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (right + left) // 2                       # mid : 3-idx  ( 요소값 7 )
            mid_pivot = (mid + pivot) % len(nums)           # mid_pivoit : mid위치에서 pivot만큼 이동하고, 배열 길이를 초과할 경우 회전해야하므로 (%)나머지값으로 처리

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1
    
# other
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid  = (left+right)//2
            if nums[mid] == target:
                return mid
            
            #case 1 left sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
                    
            #case 2 right sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1


# failed
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<2 :
            return 0 if target ==nums[0] else -1

        left, right = 0, len(nums)-1
        
        while left <= right :
            mid = (right+left)//2

            if nums[left] == target :
                return left
            if nums[right] == target :
                return right

            if nums[mid] == target :
                return mid
            elif nums[mid] > target > nums[left] or (nums[mid] < target and target > nums[right]):
                right = mid -1
            elif nums[mid] > target and target < nums[left] or (nums[mid] < target < nums[right]) :
                left = mid + 1
            else :
                return -1
        
        return -1