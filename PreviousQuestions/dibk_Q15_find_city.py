'''
🍪문제 번호 :
13장 DFS/BFS - 15 : 특정 거리의 도시 찾기
https://www.acmicpc.net/problem/18352

🍈문제 정의 :
N개의 도시와 M개의 단방향 도로가 존재하고(거리는 1), X도시로부터 출발하여 최단거리가 K인 도시번호를 모두 출력하기

🍊풀이 시간 :
40분(예제는 오케이, 백준failed)

🍒풀이 방법 :
1.재귀함수를 생성하고(입력값 : X,깊이(거리)값)
2.결과값 딕셔너리를 정의하여 key(도시번호), value(거리==깊이)로 설정
3.결과값 딕셔너리에서 K거리와 같은 도시번호만 print로 출력

-재귀함수에서 결과값 딕셔너리 정의를 key와 value값을 반대로 설정한 실수.
-재귀함수를 실행하며 말단 노드로 도착해야 딕셔너리 값설정을 했는데, 문제를 다시 읽어보니 해당 도시 도착한 최단거리를 다 저장해야했음(예제3번문제에서 실수확인)
-백준에서 런타입에러(recursionError)가 뜨는데, https://help.acmicpc.net/judge/rte/RecursionError
위 해결법으로 설정해봤지만 메모리 초과.....
재귀함수를 쓰지 않는 게 해결법이라니,,,

'''
import sys
sys.setrecursionlimit(10**9)

N,M,K,X = map(int,sys.stdin.readline().split()) #
graph = {}

for _ in range(M):
    start,end =map(int,sys.stdin.readline().split())
    graph[start] = graph.get(start,[]) + [end]

info = {}

def recursive(x,dist):
    if x not in info.keys():
        info[x] = dist
    else :
        info[x] = min(dist,info[x])
        
    if x not in graph :
        return
    
    dist+=1
    for next in graph[x] :
        recursive(next,dist)

    return

recursive(X,0)

trigger = False
for node,dis in info.items():
    if dis == K :
        trigger = True
        print(node)

if not trigger :
    print(-1)
    