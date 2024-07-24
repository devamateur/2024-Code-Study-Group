'''
🍪문제 번호 :
8장 실전문제 - 바닥 공사

🍈문제 정의 :
가로길이N, 세로길이 2인 직사각형 바닥에 3가지 덮개를 이용하여 채우기
1X2, 2X1, 2X2

🍊풀이 시간 :
failed

🍒풀이 방법 :
경우의 수 문제, Nx2행렬

- 1X2 : (N-1)공간 1가지
- 2X1 : (N-2)공간 2가지
- 2X2 : (N-2)공간 1가지

point. 위 문제가 점화식을 세울 수 있다는 것. : a_i = a_i-1 + (2*a_i-2)

'''

class Solution :
    
    def flooringWork(self):
        # 입력
        N = int(input("가로 길이 입력 : "))
        # 1이하 제외
        
        dp = [0]*(N+1)
        
        dp[1] = 1           # 2X1
        dp[2] = 3           # 1X2(2), 2X2
        
        for i in range(3,N+1):
            dp[i] = (dp[i-1] + 2*dp[i-2])%796796

        print("결과 : ",dp[N])
        return 
    
test = Solution()
test.flooringWork()