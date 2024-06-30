# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/
# [문제] 유효한 괄호 : 괄호로 된 입력값이 올바른지 판별하라.
class Solution:
    def isValid(self, s: str) -> bool:
        # 입력값이 홀수면 무조건 Falsd
        if len(s)%2 !=0 : return False
        
        pair_table = {')':'(',"}":"{",']':'['}
        ans = []
        
        for ch in s: 
            if ch not in pair_table :
                ans.append(ch)
            
            # 이 부분에서 헤맴.
            elif not ans or pair_table[ch] !=ans.pop():
                return False
        
        return True if not ans else False


'''
해당 코드는 아래 예제에서 Worng.
문제를 잘 못 이해.
페어만 맞는 게 아니라, 순서도 맞아야함 --> ([])

s = "([)]"

class Solution:
    def isValid(self, s: str) -> bool:
        # 입력값이 홀수면 무조건 Falsd
        if len(s)%2 !=0 : return False
        
        change_ch = {')':'(',"}":"{",']':'['}
        count_ch = {}

        for idx in range(len(s)) :
            ch = s[idx]
            if ch in change_ch.keys():
                ch = change_ch[ch]
            
            if ch not in count_ch.keys():
                count_ch[ch] = 0
            count_ch[ch] +=1
        
        for val in count_ch.values():
            if val%2 !=0:
                return False
        return True
        
'''