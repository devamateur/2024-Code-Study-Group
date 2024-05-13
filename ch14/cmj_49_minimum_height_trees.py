import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        count = collections.defaultdict(list)
        degree = collections.defaultdict(int)   # 그래프의 차수를 저장

        for x, y in edges:
            count[x].append(y)
            count[y].append(x)
            degree[x] += 1
            degree[y] += 1

        deq = collections.deque()

        # 큐에 리프노드를 추가함
        for num in range(n):
            if degree[num] == 1:        # 리프노드
                deq.append(num)
        
        while n > 2:
            curr_size = len(deq)
            n -= curr_size          # 전체 노드 수 - 리프 노드 수

            for _ in range(curr_size):     # 리프노드들을 제거
                leaf = deq.popleft()

                for y in count[leaf]:
                    degree[y] -= 1  # 연결된 노드의 차수 감소
                    if degree[y] == 1:  # 새로운 리프 노드 = 즉, while문이 끝나는 시점에서의 루트 노드
                        deq.append(y)
        return list(deq)

    '''def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        count = collections.defaultdict(list)
        if n == 1:
            return [0]
        if n == 2:
            return sum(edges, [])       # 일차원 리스트로 변환

        # 각 노드와 연결된 노드를 딕셔너리 형태로 저장
        for x, y in edges:
            count[x].append(y)
            count[y].append(x)
        
        # 딕셔너리를 빈도수 내림차순으로 정렬
        count = dict(sorted(count.items(), key=lambda x:len(x[1]), reverse=True))

        # 루트 노드
        if [key for key in count.keys()][1] > [key for key in count.keys()][2]:
            return [key for key in count.keys()][:2]
        return [[key for key in count.keys()][0]]'''