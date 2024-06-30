# 316. Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/description/

# 다시 풀기
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans = []
        counter = {}

        for ch in s :
            if ch not in counter.keys():
                counter[ch] = 0
            counter[ch]+=1

        for ch in s :
            counter[ch] -=1
            if ch not in ans :
                while ans and ch < ans[-1] and counter[ans[-1]] > 0:
                    ans.pop()

                ans.append(ch)

        return ''.join(ans)


# solution
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []        # { a : 1, b:2, c:2

        # s = "bcabc"
        for ch in s :
            counter[ch] -=1                                         # 1. counter > b:1     2. > c:1       3. > a:0      4. b:0
            if ch in seen :     
               continue
            
            while stack and ch < stack[-1] and counter[stack[-1]] > 0:      # 3. seen : b,  seen : 
                seen.remove(stack.pop())
            
            
            stack.append(ch)                                        # 1.stack : b   2. : b,c   3. : a       4. a,b,c >>> a,b,c
            seen.add(ch)                                            # 1. seen : b   2. : b,c   3. : a
        
        return ''.join(stack)