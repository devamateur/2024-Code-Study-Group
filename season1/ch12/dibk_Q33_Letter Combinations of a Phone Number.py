'''
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

[문제] 2-9 숫자가 주어졌을 때, 전화번호로 조합 가능한 모든 문자를 출력하라.
'''

# solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits : return []
        
        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []

        # input = '23'
        def recursive_dfs(idx,path):            # index, path(이미확인한 문자)
            if len(path) == len(digits) :
                ans.append(path)
                return

            for i in range(idx, len(digits)) :      # 1. 0~2까지 순회, i=0
                for j in phone[digits[i]] :         # 1. digits[0] == '2', phone['2']=='abc', j=='a'
                    recursive_dfs(i+1,path+j)       # 1. idx==1, path =='a'
            return

        recursive_dfs(0,'')
        return ans
    