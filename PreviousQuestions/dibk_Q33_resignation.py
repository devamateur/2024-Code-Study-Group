'''
🍪문제 번호 :
16장 DP - 퇴사
https://www.acmicpc.net/problem/14501

🍈문제 정의 :
입력값은
상담 완료하는 시간T, 상담료P로 이뤄진 값
스케쥴러표를 확인하여 최대 수익을 구할 수 있게 구하기

🍊풀이 시간 :
34~

🍒풀이 방법 :
리트코드의 우주최강 도둑놈, 식량 문제 그거랑 비슷한 것 같다. > DFS??

'''
# 입력
n = int(input())
schedule_talbe = []
for _ in range(n):
    schedule_talbe.append(list(map(int, input().split())))

# 함수
def recursive(idx):
    if idx+schedule_talbe[idx][0] > n :
        return 0
    
    accumulation = schedule_talbe[idx][1]                   # 해당 인덱스(day)의 상담료
    accumulation +=recursive(schedule_talbe[idx][0]+idx)
    return accumulation

result = []
for i in range(n) :
    result +=recursive(i),

print(max(result))

'''
# 답지
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
'''