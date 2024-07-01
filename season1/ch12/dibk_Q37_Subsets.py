'''
78. Subsets
https://leetcode.com/problems/subsets/description/
[time] 15m
[문제]  모든 부분 집합을 리턴하라
[풀이방식]
- Q35와 비슷하지만 ans의 저장 위치가 중요한 포인트
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recursive(idx,tmp):
            ans.append(tmp)

            for i in range(idx,len(nums)):
                recursive(i+1,tmp+[nums[i]])
            return

        recursive(0,[])

        return ans