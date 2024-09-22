'''
🍪문제 번호 :
12장 구현 - 07 : 럭키 스트레이트
https://www.acmicpc.net/problem/18406

🍈문제 정의 :
어떤 게임의 캐릭터 기술로 럭키 스트레이트라는 게 있다. 해당 기술은 특정 조건이 만족될 때 사용가능하다.
캐릭터 점수N은 자릿수 기준으로 반으로 나누어 왼쪽부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수 합을 더한 값이 동일한 상황을 의미
ex) 123,402 = (1+2+3) (4+0+2) > 럭키 스트레이트 사용 가능
현재 N점수가 주어졌을 때 럭키 스트레이트 기술을 사용할 수 있는지 출력하는 프로그램 구하기

🍊풀이 시간 :
5분

🍒풀이 방법 :
입력값을 문자열로 받아서, 해당 입력값의 중간 인덱스 위치를 구하고, 왼쪽/오른쪽으로 문자열을 저장한다.
왼/오 배열을 같이 for문 순회해서 양쪽의 총합을 구한 후, 비교하여 출력

'''
import sys

N = str(sys.stdin.readline().rstrip())
mid_idx = int(len(N)//2)

left = N[:mid_idx]
right = N[mid_idx:]

left_result,right_result = 0,0
for lnum,rnum in zip(left,right):
    left_result +=int(lnum)
    right_result +=int(rnum)

if left_result == right_result :
    print("LUCKY")
else :
    print("READY")