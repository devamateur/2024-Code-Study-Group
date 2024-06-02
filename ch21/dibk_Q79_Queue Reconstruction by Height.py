'''
406. Queue Reconstruction by Height
https://leetcode.com/problems/queue-reconstruction-by-height/description/

[time] 20m
[문제] people리스트에는 [키, 앞에 자기보다 큰 사람 수] 값이 존재하는데, 이를 정렬하기.
[풀이방식] :
- heap을 활용하려고 했는데, heapify : O(NlogN)
- sort함수도 O(NlogN)라서 sort사용
- 포인터를 활용, while+for 이중for문 활용 + 슬라이싱 활용 >> 시간 복잡도가 높은 편

# solution : leetcode
- 생각의 발상 : h기준 내림차순, k오름차순으로 정렬 후, insert함수를 활용하여 정렬

'''

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : x[1::-1])              # [h,k]에서 k기준으로 오름차순 정렬
        result = []
        
        for h,k in people :
            if k == 0 :                                     # k가 0일때, 무조건 저장
                result += [h,k],
                continue

            count = k                                       # 횟수 저장
            for idx in range(len(result)):              
                if result[idx][0] >=h :                     # 높이가 큰 경우 count 감소
                    count-=1
                
                if count<0 :                                # 음수가 된 순간
                    result = result[:idx] + [[h,k]] + result[idx:]      # 해당 값을 넣기
                    break                                               # 슬라이싱 시간 복잡도 O(N)
            else :
                result += [h,k],
        
        return result

# solution
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))  # [h,k]에서 h로 먼저 내림차순, k로 오름차순
        result = []

        for p in people:
            result.insert(p[1], p)              # insert :: O(N)

        return result