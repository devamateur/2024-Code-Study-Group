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

    ''' 투포인터를 이용해 문자열의 중앙에서 확장하는 방법 '''
    def center_expansion(self, s: str) -> str: 
        
        # 팰린드롬일 경우 투포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]         # 조건을 만족하지 않는 경우 확장한 양 옆을 제외해서 리턴

        # 예외 케이스의 경우 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        
        window = ""
        # 슬라이딩 윈도우가 우측으로 이동
        # 길이가 2인 포인터 / 3인 포인터 사용
        for i in range(len(s)):
            window = max(window, expand(i, i+1), expand(i, i+2), key=len)

        return window