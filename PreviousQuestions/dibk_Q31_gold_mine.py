'''
🍪문제 번호 :
16장 DP - 금광

🍈문제 정의 :
NXM크기의 금광은 1X1큭기 칸으로 나눠져 있고, 각 칸에 특정 크기의 금이 있다.
맨 첫번째 열의 어느 행에서든 출발하여 m번의 움직임(3가지) 중 하나의 위치로 이동해야 한다. 겨로가적으로 얻으 수 있는 금 최대 크기를 출력하기

🍊풀이 시간 :
failed

🍒풀이 방법 :
움직임에 대해 설정하고(좌표), 그리디하게 현재 위치에서 가장 큰 값을 찾도록 함.
> 리스트를 배열로 바꾼 다음에 확인할까? 아니면 수열 자체로 보고 진행을 할까? > 수열로 생각해서 풀어보기
>> 이걸 어떻게 구현하지????

solution :
2차원 배열로 생성, 3가지 위치(오른쪽위,오른쪽,오른쪽 아래)의 값 중에서 max값을 찾고, 2차원 배열 가장 맨 오른쪽 아래에 최대값을 저장함.

'''
# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화 : 여기가 포인트구나..
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 이 부분은 좀 꼬인다.
    
    # 다이나믹 프로그래밍 진행          : m열에 도달하면 움직임이 멈춤
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]          # 아, 좌표 이용
                
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)




'''
class Solution :
    def run(self) :
        N,M = map(int(input().split()))
        elements = list(map(int(input().split())))\
        
        result = 0
        
        #첫 시작점
        0,4,,,,
        
        
    
    def gold_mine(self):
        # 설정
        import sys
        input = sys.stdin.readline      # 나중에 백준에서 이렇게 설정하고 input함수 사용해보기
        
        movement = [(-1,1),(0,1),(1,1)]     # 오른쪽위, 오른쪽, 오른쪽 아래
        answer = []
        
        # 입력
        T = int(input())
'''