class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []

        # 1. 그래프로 만듦
        graph = {}
            
        for i in range(len(tickets)):
            if tickets[i][0] not in graph:
                graph[tickets[i][0]] = []
            if tickets[i][0] in graph:
                graph[tickets[i][0]].append(tickets[i][1])
            
        # 2. 도착지를 사전순으로 정렬
        for node in graph:
            graph[node].sort()

        def dfs(start):         # 3. 그래프 탐색
            if start not in graph:         # 도착지가 없으면 결과에 추가하고 바로 리턴
                result.append(start)
                return

            while graph[start]:
                dfs(graph[start].pop(0))         #### 도착지를 다시 출발지로 설정
            result.append(start)
            
        dfs("JFK")

        return result[::-1]
    
    '''def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        visited = [False]*len(tickets)*2

        def dfs(source):         # dfs로 어떻게 풀어야할지 감이 잘 안옴

            for i in range(source, len(tickets)):
                if i == 0:
                    if tickets[i][0] == "JFK":
                        result.append(tickets[i][0])
                else:
                    if tickets[i][0] not in result and tickets[i][0] in tickets[i]:
                        result.append(tickets[i][0])
                        #dfs(i)
                    if tickets[i][1] not in result and tickets[i][1] in tickets[i]:
                        result.append(tickets[i][1])
                        #dfs(i)
            return result
        
        dfs(0)

        return result'''