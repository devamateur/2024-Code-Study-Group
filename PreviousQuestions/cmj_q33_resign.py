class Solution:
    def find(self):
        '''
            N+1일째에 퇴사한다고 할 때,
            상담으로 얻을 수 있는 최대 수익을 구하는 문제
            (단, N일이 지나면 상담할 수 없음)

            Ti: i번 상담을 완료하는 데 걸리는 시간, Pi: i번 상담을 했을 때 받는 금액

            상담 시간은 작을수록 금액은 클수록 좋다
        '''
        # N: 상담의 개수, N일이 지나면 상담할 수 없음
        N = int(input())

        # Ti: 상담을 완료하는 데 걸리는 기간, Pi: 상담을 했을 때 받을 수 있는 금액
        dp = [[0]*(2) for _ in range(N+1)]

        for i in range(N):
            t, p = map(int, input().split())
            dp[i] = [t, p]

        max_val = 0
        gap = 0
        for i in range(N-1, -1, -1):        # 상담 기간을 벗어나는 경우 0값으로 초기화하기 위해 뒤에서부터 시작
            gap = i+dp[i][0]
            if gap <= N:
                dp[i][1] = max(dp[gap][1]+dp[i][1], max_val)
                max_val = dp[i][1]            ### 최댓값을 중간중간 저장하는 이 부분을 놓쳐서 못풀었음..
            else:              # 범위를 벗어나는 경우, 그냥 max_val값으로 초기화(max_val: 현재까지의 최대 금액)
                dp[i][1] = max_val
        print(max(dp, key=lambda x:x[1])[1])

s = Solution()
s.find()