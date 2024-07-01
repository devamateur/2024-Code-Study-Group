'''
75. Sort Colors
https://leetcode.com/problems/sort-colors/description/

*one-pass algorithm? : 입력을 정확히 한 번 읽는 스트리밍 알고리즘


[time] 3m
[문제] sort함수를 사용하지 않고 리스트 값 정렬하기
[풀이방식]
- 62번 문제풀이를 활용함.
    - 앞에서 뒤까지 가는 인덱스 i와 값을 비교하며 앞쪽으로 이동하는 인덱스 j를 활용하여, 값 비교 후 자리 바꿈.
- 답지 솔루션의 경우, 해당 문제에서만 활용 가능한 솔루션으로 보임.
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and nums[j-1] > nums[j] :
                nums[j-1],nums[j] = nums[j],nums[j-1]
                j-=1
            
            i+=1

        return 