'''
🍪문제 번호 :
11장 그리디 - 03 : 문자열 뒤집기
https://www.acmicpc.net/problem/1439

🍈문제 정의 :
0,1로 이뤄진 문자열S가 주어졌을 때, 해당 문자열을 모두 같은 숫자로 만들려고 함.

🍊풀이 시간 :
40~

🍒풀이 방법 :
easy~

'''
import sys

S = str(sys.stdin.readline().rstrip())

# if S.count(1)==len(S) or S.count(0) == len(S):
#     print(0)

zero,one = 0,0
tmp = int(S[0])

if  tmp == 0 :
    zero +=1
else :
    one +=1

for i in range(1,len(S)):
    if int(S[i]) == tmp :
        

