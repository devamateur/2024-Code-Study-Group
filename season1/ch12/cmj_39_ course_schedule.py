import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프 구성
        graph = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)  # 각 노드의 진입차수(in-degree): 각 노드에 연결된 엣지 수

        for x, y in prerequisites:
            graph[y].append(x)  # y에서 x로 에지 추가
            in_degree[x] += 1   # x 노드의 진입차수 증가

        # 진입차수가 0인 노드를 큐에 추가
        queue = collections.deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        # BFS를 사용하여 노드 순환 구조 확인
        visited_count = 0  # 방문한 노드의 수를 추적

        while queue:
            course = queue.popleft()  # 큐에서 첫 번째 노드를 추출
            visited_count += 1

            # 인접 노드의 진입차수를 감소시키고, 0이 되면 큐에 추가
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 방문한 노드의 수가 주어진 코스 수와 같다면, 순환 구조가 없다는 의미
        return visited_count == numCourses

    '''
    48 / 52 testcases passed
    dfs는 time limit에 걸림
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True