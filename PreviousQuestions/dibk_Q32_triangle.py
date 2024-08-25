'''
🍪문제 번호 :
16장 DP - 정수 삼각형
https://www.acmicpc.net/problem/1932

🍈문제 정의 :
삼각형으로 나열된 입력값에서 맨위에서부터 선택된 수의 합이 최대가 되는 경로를 구하기.

🍊풀이 시간 :
25분

🍒풀이 방법 :
31번 문제와 같은 풀이방법으로 해결함.
검색 중 다른 솔루션 발견.

'''

n = int(input())
triangle = []
for _ in range(n):
    triangle += list(map(int(input().split()))),

for row in range(1, n):
    for col in range(row + 1):

        if col == 0:
            up_left = 0                     # 왼쪽 위(대각선위)
        else:
            up_left = triangle[row - 1][col - 1]

        if col == row:
            up = 0
        else:
            up = triangle[row - 1][col]

        triangle[row][col] = triangle[row][col] + max(up_left, up)

print(max(triangle[n - 1]))


## other
# https://hyonu.tistory.com/36?category=1409003
N = int(input())
DP = [[0]+list(map(int,input().split()))+[0] for _ in range(N)]

for r in range(1,N):
    for c in range(1,len(DP[r])-1):
        DP[r][c] += max(DP[r-1][c-1], DP[r-1][c])

print(max(map(max,DP)))