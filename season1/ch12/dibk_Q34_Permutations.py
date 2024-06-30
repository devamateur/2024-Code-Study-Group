'''
46. Permutations
https://leetcode.com/problems/permutations/description/
[time] 25m
[문제] 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.
[풀이방식]
- Q33번 풀이방식을 활용함
    - visited(방문했던 변수)가 조합 갯수만큼되면 저장하고 리턴
    - 재귀를 돌 때, 방문했건 기록을 담는 변수visited와 앞으로 방문할 변수(tmp)를 활용하여 재귀

'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recursive_dfs(visited, tmp):        # visited(list) 방문했던 기록을 담는 변수, tmp(list) 앞으로 방문할 데이터를 담는 변수
            if len(visited)==len(nums):
                ans.append(visited)
                return

            for i in range(len(tmp)):
                recursive_dfs(visited+[tmp[i]],tmp[:i]+tmp[i+1:])
            return
        
        for idx in range(len(nums)):
            recursive_dfs([nums[idx]],nums[:idx]+nums[idx+1:])

        return ans