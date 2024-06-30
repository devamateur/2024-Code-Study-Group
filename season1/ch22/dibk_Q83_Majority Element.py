'''
169. Majority Element
https://leetcode.com/problems/majority-element/description/

[time] 3m
[문제] 입력 리스트 내에서 가장 많은 빈도의 요소를 구하기
[풀이방식] :

'''
# 분할정복
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]


# 다이나믹
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:        # 전체크기보다 많아지느 순간 return
                return num

# 파이써닉..? 통계적인 방법론
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums :
            nums_dict[num] = nums_dict.get(num,0)+1

        return max(nums_dict, key =nums_dict.get)
    
