class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g: 아이가 원하는 쿠키 개수
        # s: 각 쿠키의 수

        # 오름차순 정렬
        g.sort()
        s.sort()
        
        count = 0

        p1 = p2 = 0       # 두 배열 g, s의 인덱스

        while p1<len(g) and p2<len(s):
            if s[p2] >= g[p1]:       # 쿠키의 개수가 많은 경우, 카운트를 증가시키고 두 배열 모두 다음 원소로
                count += 1 
                p1 += 1
                p2 += 1

            else:
                p2 += 1           # 쿠키의 개수가 적으면, 쿠키 배열 s만 다음 원소로 이동
                
        return count