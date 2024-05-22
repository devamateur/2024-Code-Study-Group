'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/description/

[time] failed
[문제] 간격 배열(리스트)가 주어졌을 때, 겹치는 간격은 합치고 겹치지 않는 부분들도 반환하기
[풀이방식]
- 입력 리스트의 첫번째 값을 기준으로 정렬
- 입력 리스트를 순회할 때, start값이 merged의 끝값의 end값보다 작아야 해당 구간안에 들어감.
    - max함수로 end값을 결정
'''

# solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key = lambda x : x[0])           # 정렬

        for s,e in intervals :
            if merged and s <= merged[-1][1] :          # start가 merged의 끝값의 end값보다 작아야 해당 구간안에 들어감.
                merged[-1][1] = max(merged[-1][1],e)    # max로 end값 비교
            else :
                merged +=[s,e],                         # += [s,e], : 쉼표 중요
        
        return merged


# failed 
import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <=1 : return intervals

        heapq.heapify(intervals)
        result = []
        tmp = heapq.heappop(intervals)
        
        for _ in range(len(intervals)):
            s,e = heapq.heappop(intervals)

            if s > tmp[1] :
                tmp = [s,e]

            elif s < tmp[1] and e < tmp[1] :
                pass

            elif s <= tmp[0] :
                tmp[0] = s
            
            elif e >= tmp[1] :
                tmp[1] = e
            
            result.append(tmp)
        
        return result
            