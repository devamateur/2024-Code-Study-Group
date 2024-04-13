'''
771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/description/

[문제] J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개 있는가?
time : 5m
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_table = {ch:0 for ch in jewels}
        
        for ch in stones :
            if ch in j_table.keys() :
                j_table[ch] +=1
        
        return sum(j_table.values())
    
    
# other Solution
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_table = {ch for ch in jewels}
        ans = 0
        
        for ch in stones :
            if ch in j_table:
                ans +=1
        
        return ans