'''
🍪문제 번호 :
18장 그래프 이론 - 45번 최종 순위
https://www.acmicpc.net/problem/3665

🍈문제 정의 :
N개의 팀이 대회에 참가했다. 올해는 최종 순위를 발표하지 않지만 작년에 비해 상대적인 순위가 바뀐 팀의 목록만 발표한다(작년과 올해의 참가 팀이 동일함)
위 정보만으로 최종 순위를 만들기


🍊풀이 시간 :

🍒풀이 방법 :
- 위상 정렬 알고리즘?

'''

import sys

testcase = int(sys.stdin.readline().rstrip()) # 테스트 케이스 개수
result = []

for _ in range(testcase) :
    N = int(sys.stdin.readline().rstrip()) # 팀의 수
    ti = list(map(int,sys.stdin.readline().split()))   # 순서대로 i등 번호
    m = int(sys.stdin.readline().rstrip()) # 상대적인 등수가 바뀐 쌍의 수
    
    if m == 0 :
        result += [ti],
        continue
    
    info = {}
    for __ in range(m):
        a,b = map(int,sys.stdin.readline().split())
        