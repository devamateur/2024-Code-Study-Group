'''
🍪문제 번호 :
17장 최단경로 - 38번 화성 탐사

🍈문제 정의 :
화성 탐사 기계가 존재하는 공간이 NXN크기의 2차원 공간이고 각 칸을 지나기 위한 비용이 존재한다.
가장 왼쪽 위 칸에서 가장 오른쪽 아래칸 까지  이동하는 최송 비용을 출력하는 프로그램 작성하기

🍊풀이 시간 :
faild

🍒풀이 방법 :
- 구현+재귀문제로 해석되었음. but failed...
- 다익스트라 알고리즘 : 단계마다 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택 한 뒤에, 최단거리 갱신하는 방법(우선순위 큐 사용)

상하좌우로 움직이며 그리디하게 찾아가는 구현 풀이를 먼저 생각했으나, 각 루트마다 최소비용 누계값이 달라 질 것 같아서 재귀(bfs)를 생각했다. 하지만 해당 방법은 시간 제한에 걸릴 것 같아서 실패
다익스트라 알고리즘 풀이에서 핵심은 최단 거리 테이블, 힙큐를 활용한 부분으로 생각된다.

'''

import heapq
import sys
input = sys.stdin.readline      # 나중에 백준에서 이렇게 설정하고 input함수 사용해보기
INF = int(1e9) 

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for _ in range(int(input())):           # 테스트 케이스 숫자만큼 for문 반복
    
    n = int(input())

    # 전체 맵 정보를 입력
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    # 최단 거리 테이블 : 최단 거리를 구해야함으로 무한값으로 초기화
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0 
    
    q = [(graph[x][y], x, y)]           # [비용,row,col]
    distance[x][y] = graph[x][y]        # (0,0)위치의 초기 비용 설정

    # 다익스트라
    while q:
          # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
          dist, x, y = heapq.heappop(q)
          # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
          if distance[x][y] < dist:
              continue
          
          # 상하좌우 확인
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              # 맵의 범위를 벗어나는 경우 무시
              if nx < 0 or nx >= n or ny < 0 or ny >= n:
                  continue
              cost = dist + graph[nx][ny]
              # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
              if cost < distance[nx][ny]:
                  distance[nx][ny] = cost
                  heapq.heappush(q, (cost, nx, ny))

    print(distance[n - 1][n - 1])
    

class Solution :
    def run(self,n):
        n_map = []
        for _ in range(n) :
            n_map += list(map(int,input().split())),

        # n_map을 움직이며 그리디하게 최소값을 찾아가는 코드를 작성하려고 했으나
        # 해당 문제는 최단경로 문제인데, 원하는 풀이가 아닌 것 같아서 중단
        
        return
    
    def exploration(self):
        
        result = []
        
        # 입력
        T = int(input().rstrip())
        
        for _ in range(T) :
            N = int(input().rstrip())
            
            result += self.run(N),
            
    
test = Solution()
test.exploration()
