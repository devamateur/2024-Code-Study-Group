'''
🍪문제 번호 :
10장 실전문제 - 도시 분할 계획   
https://www.acmicpc.net/problem/1647

🍈문제 정의 :
마을에 N개의 집, M개의 연결통로(양방향), 각 길마다 유지비(cost)가 있다.   
마을을 두 개의 마을로 분할할 계획인데, 분할된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야하며 길을 없앨 수 있고 마을에는 집이 하나 이상 있어야한다.(제약조건)
최소 유지비를 구하기.   
그래서 탈출한 원숭이랑 도시 분할 계획의 관계는 뭐지?   

즉, 두 뭉터기로 나누고 뭉터기 안의 집들은 연결되어있지만 두 뭉터기는 연결 안돼도 된다는 뜻?

🍊풀이 시간 :
failed

🍒풀이 방법 :
https://ji-gwang.tistory.com/460
알고리즘 이론 공부를 다시 해야겠다.

'''

class Solution :
    def cityDivisonPlan(self):
        # 입력
        N, M = map(int, input().split())

        graph = []
        parent = [i for i in range(N + 1)]  # 부모를 저장
        rank = [0] * (N + 1)  # 각 노드마다 랭크를 저장
        
        # 함수
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union_(a, b):
            a = find(a)
            b = find(b)

            # 이미 부모가 같다면 리턴
            if a == b:
                return

            if rank[a] > rank[b]:
                parent[b] = a
            elif rank[a] < rank[b]:
                parent[a] = b
            else:
                parent[a] = b
                rank[b] += 1
        
        # run
        for _ in range(M):
            a, b, cost = map(int, input().split())
            graph += (a,b,cost),
        
        graph.sort(key=lambda x : x[2])     # cost 기준 작은값부터
        
        ans = 0  # 연결된 마을 길이의 합
        end_v = 0  # 마지막에 연결된 마을 길이를 저장
        for i in graph:

            if find(i[0]) != find(i[1]):
                union_(i[0], i[1])
                ans += i[2]  # 마을의 연결 비용들을 계속 더해주고
                end_v = i[2]  # 마지막에 연결된 마을 연결 비용을 저장

        print(ans - end_v)  # 마지막에 연결된 연결 비용만 빼준 체 출력
        return 
    
test = Solution()
test.cityDivisonPlan()


# soluteion
'''
from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

topology_sort()
'''