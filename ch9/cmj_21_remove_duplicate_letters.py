import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []    #### seen: 봤던 알파벳을 저장하는 셋

        for char in s:
            counter[char] -= 1
            if char in seen:     # 이미 본 알파벳은 skip
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
    
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