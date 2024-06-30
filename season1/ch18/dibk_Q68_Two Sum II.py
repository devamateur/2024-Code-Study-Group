'''
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

[time] 4m
[문제] 
[풀이방식] :
- 이진 탐색 알고리즘 활용

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 2 : return [1,2]

        left,right = 0, len(numbers)-1

        while left<right :
            
            if numbers[left] + numbers[right] == target :
                return [left+1,right+1]
            elif numbers[left] + numbers[right] < target :
                left +=1
            else :
                right -=1
        
        return -1