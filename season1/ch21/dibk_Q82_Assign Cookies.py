'''
455. Assign Cookies
https://leetcode.com/problems/assign-cookies/description/

[time] failed
[문제] 아이들의 식탐 요소를 담은 g리스트와 쿠키의 크기를 담은 s리스트가 존재한다. 최대로 만족할 수를 출력.
[풀이방식] :
- 문제가 쓰잘데기 없이 스토리적이다. 나는 내 자식들에게 탐욕지수 따윈 관계 없이 쿠키를 주지 않을거시다.
- 그리디 문제를 3문제 풀면서 느낀점은, 문제 내에서 신박한 루틴을 창조하여 코드 작성하는 능력을 키우는 것 같다.
- 각 g,s를 정렬 후, 쿠키 크기가 더 큰 경우에만 아이의 위치를 바꿈. 쿠키는 계속 이동
- 쿠키를 기준으로 움직일지, 아이를 기준으로 할 지 고민했었는데, 쿠키가 아이의 탐욕을 맞추지 못해도 다음 쿠키로 넘어갈 수 있지만 아이의 위치는 쿠키가 맞아야 움직이는구나..
'''
#
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        # 만족하지 못할 때까지 그리디 진행
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:       # 쿠키의 크기가 아이의 크기보다 클 때, 다음 아이
                child_i += 1
            cookie_j += 1                       # 쿠키의 다음 크기를 찾으러 이동.

        return child_i


#
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or not g : return 0
        q = deque(s)

        cookies = q.popleft()
        ans = 0
        g.sort()
        for i in range(len(g)):
            if g[i] <= cookies:
                ans+=1
                if not q : break

                cookies = q.popleft()
                
        
        return ans





