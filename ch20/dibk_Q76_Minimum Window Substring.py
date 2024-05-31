'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/description/

[time]
[문제] 부분 문자열이 포한된 최소 윈도우 문제로, t의 모든 문자열이 포한된 s의 부분 문자열을 구하기.
[풀이방식] :

'''

# failed
import re
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t : return s
        if len(s) <= len(t) : return ""
        
        t_dict = {}
        indices = []

        for ch in t :
            if ch not in t_dict :
                t_dict[ch] = 0
            t_dict[ch]+=1

            for idx, val in enumerate(s):
                if val == ch:
                    indices.append(idx)
        indices.sort()

        end,start = indices.pop(),indices.pop()
        
        while indices :
            if end-start+1 < len(t) :
                start = indices.pop()
            else :
                return s[start-1:end+1]