'''
🍪문제 번호 :
14장 정렬 - 23 : 국영수
https://www.acmicpc.net/problem/10825

🍈문제 정의 :
조건에 맞게 학생들 성적을 정렬하기

🍊풀이 시간 :
14분

🍒풀이 방법 :
"1.국어 점수가 감소하는 순서로" --> 왜 이렇게 표현하지? 내림차순이라고 하면 되는디

sort함수로 바로 정렬

'''
import sys

N = int(sys.stdin.readline().rstrip()) #
info = []

for _ in range(N):
    name,korean,english,math=map(str,sys.stdin.readline().split())
    info +=[int(korean),int(english),int(math),name],

info.sort(key = lambda x : (-x[0],x[1],-x[2],x[3]))

for i in info :
    print(i[-1])