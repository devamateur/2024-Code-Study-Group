'''
🍪문제 번호 :
13장 DFS/BFS - 19 : 연산자 끼워넣기
https://www.acmicpc.net/problem/14888

🍈문제 정의 :
N개의 수로 이뤄진 수열이 주어지고, 그 수 사,이에 넣을 수 있는 연산자 N-1개가 주어진다.(연산자는 +,-,X,% 4개로만 이뤄짐)
연산자 우선순위를 무시하고 앞 순서대로 계산이 진행되는데, 식의 결과가 최대인 것과 최소인 것을 구하기

🍊풀이 시간 :
40분

🍒풀이 방법 :
모든 경우의 수를 구해야하는 문제로, DFS문제라고 생각했는데 백트래킹문제라고 한다.
DFS는 모든 경우의 수를 탐색하고, 백트래킹은 모든 경우의 수를 탐색하지만 불필요한 탐색을 하지 않는다.
DFS는 원하지 않더라도 트리의 바닥까지 모두 탐색하는 것, 백트래킹은 트리거를 줘서 굳이 다 탐색하지 않는 것

백트래킹은 일반적으로 재귀형태이고, 1)재귀를 진행하는 동안 깊이를 매개변수로 사용, 2)재귀가 종료되는 시점에서 수행해하는 내용. 3)재귀가 진행중이면 가지치기(백트래킹)할 내용
으로 작성해야한다.

'''
import sys

N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
plus,minus,multip,divis =map(int,sys.stdin.readline().split())

resultMax = -1000000000                     # 최대최소 초기화
resultMin = 1000000000

def run(count,result):
    global plus,minus,multip,divis,resultMax,resultMin      # global 활용
    
    if count >= N-1 :           # N-1 계산 횟수
        resultMax = max(result,resultMax)
        resultMin = min(result,resultMin)
        return
    
    count+=1
    if plus > 0 :
        plus-=1
        run(count,result+numbers[count])
        plus +=1
    
    if minus > 0 :
        minus-=1
        run(count,result-numbers[count])
        minus +=1
        
    if multip > 0 :
        multip-=1
        run(count,result*numbers[count])
        multip +=1
        
    if divis > 0 :
        divis-=1
        run(count,int(result/numbers[count]))
        divis +=1
    
    return

run(0,numbers[0])
print(resultMax)
print(resultMin)



