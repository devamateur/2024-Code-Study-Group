class Solution:
    def calc(self):
        N = int(input())

        st = []*N

        for _ in range(N):
            name, kor, eng, math = input().split()

            st.append([name, int(kor), int(eng), int(math)])

        # 국어 내림차순, 영어 오름차순, 수학 내림차순

        st.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
        
        for s in st:
            print(s[0])

s = Solution()
s.calc()