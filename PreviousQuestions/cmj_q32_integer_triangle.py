class Solution:
    def find(self):
        N = int(input())

        dp = []          # 경로 합을 저장하는 캐시

        for i in range(N):
            line = list(map(int, input().split()))      

            dp.append(line)
        #print(dp)

        for i in range(1, N):
            for j in range(0, i+1):
                if j-1 < 0:           # 제일 왼쪽에 있는 경우
                    dp[i][j] = dp[i-1][j]+dp[i][j]          # 이전 행 왼쪽 + 현재 경로
                
                else:
                    if j+1 > i:         # 제일 오른쪽에 있는 경우
                        dp[i][j] = dp[i-1][j-1]+dp[i][j]               # 이전 행 왼쪽 + 현재 경로 (이전 행은 가로가 1씩 작으므로 j-1)
                    else:               # 가운데 경로인 경우
                        dp[i][j] = max(dp[i-1][j]+dp[i][j], dp[i-1][j-1]+dp[i][j])      # 이전 행에서 왼쪽 or 오른쪽을 택했을 경우 모두 고려

        print(max(dp[N-1]))
s = Solution()
s.find()