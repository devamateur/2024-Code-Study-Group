'''
🍪문제 번호 :
9장 실전문제 - 미래 도시

🍈문제 정의 :
1~N번 노드가 존재하고, 방문 판매원 A는 현재 1번 노드에 위치해앴으며, X번 노드에 방문하고자 한다.
노드는 양방향으로 이동이 가능하며 노드는 각자 1거리를 갖는다.
아니, 문제에서 뜬금없이 소개팅? 방문 판매원A 참 열심히 산다
A는 k번 노드(소개팅 장소) 방문하고 X번 노드를 방문해야하는데 최소 거리를 구하기

🍊풀이 시간 :
50분

🍒풀이 방법 :
1노드에서 k노드까지 가는 루트 + k노드에서 X노드까지 가는 루트를 구한다.
각 노드에서 원하는 노드까지 가는 모든 루트를 확인한 후, 최저의 길이를 리턴한다(DFS)

'''

class Solution :
    
    def futureCity(self):
        # 입력
        N, M = map(int,input("노드 갯수N, 경로의 개수M : ").split())
        
        graph = {}
        
        for _ in range(M):
            n1,n2 = map(int,input().split())
            graph[n1] = graph.get(n1,[]) + [n2]
            graph[n2] = graph.get(n2,[]) + [n1]     # 양방향
        
        x,k = map(int,input("x,k 입력 : ").split())
        visited = [False]*(N+1)
        
        def recursive(start,target):
            """
            start 출발노드
            target 목적 노드
            """
            visited[start] = True           # 해당 노드 방문 기록
            
            if start == target :
                return 0
            
            depth = 100                   # depth 개념 : 각 노드들이 DFS로 밑단까지 내려갔을 때 기록하기(==distance)
            for node in graph[start] :
                if not visited[node] :
                    distance = recursive(node,target)
                    
                    if distance !=-1 :                      # distance이 -1이면,:: node->target이 없다는 의미 
                        depth = min(depth,distance+1)
                    visited[node] = False           # 초기화
            
            return -1 if depth==100 else depth              # depth==100이면, for문을 돌아도 depth변화가 없다 == node-> target이 없다는 의미
        
        routeK = recursive(1,k)
        routeX = recursive(k,x)
 
        print("결과 : ", -1 if routeK<0 or routeX<0 else routeK+routeX)
        return 
    
test = Solution()
test.futureCity()