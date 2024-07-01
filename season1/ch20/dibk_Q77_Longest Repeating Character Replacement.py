'''
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/description/

[time] failed
[문제] k번만큼 변경으로 만들수 있는, 연속으로 반복된 문자열의 가자 긴 길이를 출력.
[풀이방식] :
- 다시 풀어보기

'''
# solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        left = 0

        for right in range(1,len(s)+1):
            frequency[s[right-1]] = frequency.get(s[right-1],0) +1
            
            max_ = max(frequency.values())

            if right - left - max_ > k :
                frequency[s[left]] -=1
                left+=1
        
        return right - left