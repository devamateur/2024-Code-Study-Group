'''
🍪문제 번호 :
14장 정렬 - 26 : 카드 정렬하기
https://www.acmicpc.net/problem/1715

🍈문제 정의 :
정렬된 숫자카드 A,B가 있다. 각 숫자카드 묶음을 최소로 비교하는 횟수를 구히기

🍊풀이 시간 :
6분 하지만 실패

🍒풀이 방법 :
입력된 숫자카드들을 정렬한 후, 작은순으로 묶어서 계산하기
실패샢넝채얓

'''
import sys

N = int(sys.stdin.readline().rstrip())
cards = []
for _ in range(N):
    cards += int(sys.stdin.readline().rstrip()),

cards.sort()
answer = cards[0]
result = 0

for i in range(1,N):
    answer += cards[i]
    result += answer

print(result)



