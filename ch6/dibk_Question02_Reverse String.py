class Solution:
    def reverseString1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """
        # s = s[::-1]
        # 공간복잡도 제한(O(1))으로 오류발생
        
        right = len(s) -1
        left = 0
        
        while left<right :
            s[left],s[right] = s[right],s[left]
            left +=1
            right -=1

'''

s.reverse()
s[:] = s[::-1]
'''
        
        