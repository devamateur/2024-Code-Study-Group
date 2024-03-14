class Solution:
    def brute_force(self, s: str) -> str:
        longest_pal=""

        # substring의 크기를 바꾸면서 팰린드롬인지 확인
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                new_s = s[i:j]
                if new_s == new_s[::-1]:
                    if len(longest_pal) < len(new_s):        ### 길이 비교
                        longest_pal = new_s

        return longest_pal