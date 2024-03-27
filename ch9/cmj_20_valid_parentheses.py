class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in range(len(s)):
            st.append(s[i])

            while len(st) >= 2 and st[-2] + st[-1] in ('()', '{}', '[]'):         # 올바른 괄호인 경우 pop
                st.pop()
                st.pop()

        return len(st) == 0     # 스택 사이즈가 0이면 True