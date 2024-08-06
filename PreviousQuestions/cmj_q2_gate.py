class Solution:
    def docking(self):

        # G: 탑승구 수, P: 비행기 수
        # 서로 다른 두 집합(탑승구/비행기)의 원소가 일대일 대응이 되어야한다

        G = int(input())
        P = int(input())

        # 각 비행기가 도킹할 수 있는 탑승구의 번호 (1~gi번)
        # ex) 4: 4번 탑승구만 도킹 가능한 게 아니라, 1~4번까지 도킹이 가능하다는 의미
        con = []        
        for _ in range(P):
            con.append(int(input()))
        
        # 방법 1. set을 사용 - 두 집합이 일대일 대응이 되어야 하므로 중복인 번호를 제거하면 결과가 나옴
        # 문제를 잘못이해... 탑승구 번호가 1~gi번까지인지 몰랐음

        # 방법 2. union-find
        def find_parent(p, node):
            if p[node] != node:
                p[node] = find_parent(p, p[node])
            return p[node]
        
        def union(p, a, b):
            a_p = find_parent(p, a)
            b_p = find_parent(p, b)

            if a_p < b_p:
                p[b_p] = a_p
            else:
                p[a_p] = b_p

        # parent: 탑승구 부모 노드
        parent = [i for i in range(G+1)]

        result = 0
        for i in range(len(con)):
            data = find_parent(parent, con[i]) # 현재 비행기의 탑승구의 루트 확인
            if data == 0: # 현재 루트가 0이라면, 종료
                break
            union(parent, data, data - 1) # 그렇지 않다면 바로 왼쪽의 집합과 합치기
            result += 1
        print('결과:', result)
s = Solution()
s.docking()