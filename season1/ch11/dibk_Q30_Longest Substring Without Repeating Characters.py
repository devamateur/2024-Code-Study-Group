'''
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


[문제] 중복 문자가 없는 가장 긴 부분 문자열 길이를 리턴하라.

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ''
        max_len = 0
        
        for ch in s :
            if ch in ans :
                idx_ = ans.index(ch)        ## input = "dvdf" 해결
                ans = ans[idx_+1:]
            
            ans+=ch
            max_len = max(max_len,len(ans))
        
        return max_len




