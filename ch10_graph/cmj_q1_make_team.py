class Solution:

    def make_team(self):
        # N: 학생(노드) 수, M: 연산 수

        N, M = map(int, input().split())
        parent = [i for i in range(N+1)]           # 각 노드의 부모를 자기 자신으로 초기화
        #print(parent)

        result = ''

        # 현재 집합 내의 부모(루트) 찾기
        # 재귀적으로 올라가면서 루트를 찾음
        def find_parent(p: list, node):
            if p[node] != node:
                return find_parent(p, p[node])
            return p[node]

        def union(p: list, a, b):
            a_parent = find_parent(p, a)
            b_parent = find_parent(p, b)

            if a_parent != b_parent:       # 두 노드의 루트가 다를 경우에만 union
                smaller = min(a_parent, b_parent)          # 두 부모 중 더 작은 숫자를 루트로
                p[a_parent] = smaller
                p[b_parent] = smaller
            return p

        for _ in range(M):
            # op: 연산 (0: 팀 합치기, 1: 같은 팀 여부 확인)
            op, a, b = map(int, input().split())

            if op == 0:
                parent = union(parent, a, b)
                print(parent)
                print()

            else:
                if find_parent(parent, a) == find_parent(parent, b):
                    result += "YES\n"
                else:
                    result += "NO\n"
            
        print(result.rstrip('\n'))

s = Solution()
s.make_team()