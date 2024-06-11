'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/description/

[time] 30m
[문제] 연속된 subtree의 최대값 구하기
[풀이방식] :
- 누적값과 순회하는 값을 비교하여 result값을 구하기.
    - 누적값보다 순회한 num이 크면 누적값을 다시 정의.

'''
# solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=1 : return nums[0]

        result = -10000
        curr = 0
        for num in nums :
            if num < curr+num :
                curr = curr+num
            else :                  # 누적값보다 순회한 num이 크면 누적값을 다시 정의
                curr = num

            if result < curr :
                result = curr
        
        return result

# 문제를 잘 못 이해한 풀이
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=1 : return nums[0]

        result = -1000
        left,right = 0,1

        tmp = nums[left]
        while right < len(nums):
            tmp += nums[right]
            
            if result <= tmp :
                result = tmp
                right +=1
            else:
                # tmp < result
                left+=1
                right = left+1
                tmp = nums[left]
            
        return result
        