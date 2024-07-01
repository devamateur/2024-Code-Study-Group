'''
39. Combination Sum
https://leetcode.com/problems/combination-sum/description/
[time] 15m
[문제]  숫자 집합을 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복으로 나열 가능하다.
[풀이방식]
- Q35와 유사한 풀이방식
    - 재귀종료코드에 elif를 추가하여 sum(tmp)값이 target값 보다 크면 재귀종료
    - for문 순회 시, 자기 자신의 인덱스를 입력값으로 가져가기(idx변수)
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def recursive(idx,tmp):             # idx인덱스, 임시저장변수tmp
            if sum(tmp) == target:          
                ans.append(tmp)
                return
            elif sum(tmp) > target :        
                return
            
            for i in range(idx,len(candidates)):
                recursive(i,tmp+[candidates[i]])
            return

        recursive(0,[])        
        return ans