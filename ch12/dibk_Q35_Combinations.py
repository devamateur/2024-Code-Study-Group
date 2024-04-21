'''
77. Combinations
https://leetcode.com/problems/combinations/description/
[time] 10m
[문제]  전체 수(n)를 입력받아 k개의 조합을 리턴하라
[풀이방식]
- Q33와 비슷한 풀이방식(재귀)
- point : for문에서 (idx, n+1) >>> 순회 시작을 1인덱스부터 시작이라 n+1까지 순회해야함.
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def recursive(idx,tmp):     # idx 인덱스, tmp 임시로 값을 담아두는 변수
            if len(tmp) == k :      # tmp의 갯수가 k개일 때,
                ans.append(tmp)     # 결과 저장
                return

            for i in range(idx,n+1):    # idx부터 n+1까지 순회 :: n까지 설정하면 마지막값을 순회할 수 없음
                recursive(i+1,tmp+[i])  # i+1부터 순회하게 하기, tmp에 i값 임시저장     ex) i:1, idx==2, tmp==[1]//     i:2, idx==3, tmp==[1,2]
            return

        recursive(1,[])

        return ans