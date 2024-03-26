class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        score = 0
        for i in range(len(s)):
            st.append(s[i])

            # 현재 괄호가 짝이 같은 괄호인 경우 스택에서 pop
            while len(st) >= 2 and st[-2] + st[-1] in ('()', '{}', '[]'):
                st.pop()
                st.pop()
            
            # 현재 괄호가 짝이 같지 않은 경우 score를 계산
            # 현재 짝이 맞지 않더라도 최종적으로 socre가 0이고 스택이 비어있으면 올바른 괄호
            if s[i] == '(':
                score += 1
            elif s[i] == '{':
                score += 2
            elif s[i] == '[':
                score += 3
            elif s[i] == ')':
                score -= 1
            elif s[i] == '}':
                score -= 2
            elif s[i] == ']':
                score -= 3

        return score == 0 and len(st) == 0