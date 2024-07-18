'''
🍪문제 번호 :
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

🍈문제 정의 :
nums 리스트는 오름차순 정렬되어 있지만 k인덱스를 기준으로 정렬되어 있다.
*ex) [2,3,4,0,1] : 3인덱스 기준으로 정렬
target값의 인덱스 찾기
*logN 시간 복잡도

🍊풀이 시간 :
failed

🍒풀이 방법 :
*min, inext함수 사용하면 금방 풀텐데,,*   
1)k인덱스 기준을 찾기 : start,end,mid값을 비교(이진탐색)하여 인덱스 위치 찾기
2) 위 기준으로 이진 탐색 진행
>> 피벗 구할 때 헷갈리고, mid_pivot이 직관적으로 이해되지 않아서 사용하기 불편함.

other solution
값을 바로 찾는 방법 : 그리디스러움.
1)처럼 mid와 end,start를 비교하며 end,start를 이동시킴. k를 찾는 것이 아니라 바로 target과 비교


'''
# solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums: return -1

        # 최소값 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # 피벗 기준 이진 검색
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                start = mid + 1
            elif nums[mid_pivot] > target:
                end = mid - 1
            else:
                return mid_pivot
        return -1
    
# other
class Solution:
    def search(self, nums: List[int], target: int) -> int:
    firstPtr, lastPtr = 0, len(nums)-1
    
    while firstPtr <= lastPtr:
        midPtr = (firstPtr + lastPtr) // 2
        if target == nums[midPtr]:
            return midPtr
        
        # check where the 0 is
        if nums[midPtr] > nums[lastPtr]:
            # 0 is on the right
            if target < nums[midPtr] and target >= nums[firstPtr]:
                lastPtr = midPtr-1
            else:
                firstPtr = midPtr + 1
        else:
            # 0 is on the left
            if target > nums[midPtr] and target <= nums[lastPtr]:
                firstPtr = midPtr+1
            else:
                lastPtr = midPtr-1
    return -1