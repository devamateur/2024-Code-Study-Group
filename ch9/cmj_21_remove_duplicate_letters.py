import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, st = collections.Counter(s), []

        for char in s:
            counter[char] -= 1       ### 현재 char의 카운트를 1 감소  
            
            if char in st:  # 이미 스택에 해당 알파벳이 있으면 skip
                continue
            
            while st and char < st[-1] and counter[st[-1]] > 0:        ### 지금 pop하려는 알파벳이 한 개 이상이어야 함
                st.pop()

            st.append(char)

        return ''.join(st)
    
'''
    166 / 290 testcases passed

    def removeDuplicateLetters(self, s: str) -> str:

        st = []      # 알파벳의 아스키코드값을 저장하는 스택
        for i in range(len(s)):
            if ord(s[i])-97+1 not in st:
                st.append(ord(s[i])-97+1)

            while len(st) >= 2 and st[0] > st[-1]:      # 스택의 맨 밑 원소가 top보다 큰 경우 pop (내림차순이 되면 안되므로)
                st.pop(0)

        # 스택의 원소를 다시 알파벳으로 변환
        for i in range(len(st)):
            st[i] = chr(st[i]+97-1)
        
        return ''.join(st)
'''