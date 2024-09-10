'''
🍪문제 번호 :
14장 정렬 - 24 : 안테나
https://www.acmicpc.net/problem/18310

🍈문제 정의 :
여러 집 중에 한 개의 집에만 안테나를 설치할 수 있다.
모든 집까지의 거리 총합이 최소가 되게 설치하기
안테나를 설치할 위치를 선택하기.

🍊풀이 시간 :
3분

🍒풀이 방법 :
이진탐색에서 "공유기 설치" 문제랑 비슷한 것 같다.

집들을 정렬한 후, 가운데 위치값을 선택하면 최소의 거리값이 나온다고 생각했다.

'''
import sys

N = int(sys.stdin.readline().rstrip()) #
info = list(map(int,sys.stdin.readline().split()))

info.sort()

print(info[(N-1)//2])
