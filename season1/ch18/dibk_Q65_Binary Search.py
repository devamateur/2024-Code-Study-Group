'''
704. Binary Search
https://leetcode.com/problems/binary-search/description/

[time] failed
[문제] 이진 탐색 알고리즘을 사용하여 target값의 위치 인덱스를 리턴하기.
[풀이방식] :
- 리스트의 앞(left), 끝(right), 중간(mid) 위치 인덱스를 활용하여 값 리턴.
- 실수한 부분 : right = len(nums) -1 / while left <= right( <가 아닌 <=)

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right :
            mid = (left+right)//2

            if nums[mid] == target : return mid

            elif nums[mid]  < target : 
                left = mid +1

            else : #elif nums[mid] > target :
                right = mid -1

        return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right :
            mid = (left+right)//2

            if nums[mid] == target : 
                return mid

            elif nums[mid] < target :
                left = mid

            else :
                right = mid
        
        return -1