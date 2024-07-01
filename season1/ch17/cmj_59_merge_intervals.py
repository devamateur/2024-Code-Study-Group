class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # start를 기준으로 오름차순 정렬
        intervals.sort()
        
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = result[-1]

            if prev[1] >= intervals[i][0]:       # 이전 구간의 end가 현재 구간의 start보다 크거나 같은 경우(겹치는 경우)
                prev[1] = max(prev[1], intervals[i][1])       # 이전 구간의 end를 max값으로 갱신
            else:
                result.append([intervals[i][0], intervals[i][1]])
                
        return result