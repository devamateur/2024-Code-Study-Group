'''
🍪문제 번호 :
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/description/

🍈문제 정의 :
요소가 좌표값인 point 배열이 있다. 원점에서 가까운 k개를 구하기(좌표 반환)

🍊풀이 시간 :
15분

🍒풀이 방법 :
좌표의 거리값을 key값, 좌표를 value값으로 설정하여 딕셔너리를 생성하고
key값을 기준으로 정렬하여 k개의 value(좌표)를 추출한다.

*딕셔너리 생성할때 value값을 리스트에 리스트를 추가했기 때문에 정렬 추출 시, extand를 활용해야 이중 리스트 문제를 벗어남
*거리값이 같은 좌표들이 있을 수 있기 때문에 마지막에 k개까지 추출함을 추가해야함.
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # 거리값 key, 좌표 value
        distance = {}
        for x,y in points :
            result = x**2+y**2
            if result not in distance :
                distance[result] = []
            distance[result] += [x,y],
            
        answer = []
        for key,value in sorted(distance.items())[:k]:      # 거리값을 기준으로 k개만큼 정렬 추출함.
            answer.extend(value)                            # value가 [[x,y]] 형태이기 때문에 answer에 append가 아닌 extand를 해줘야 이중리스트가 아닌 리스트 값이 추가됨.
        
        return answer[:k]           # 거리값 기준으로 k개를 뽑았지만, 거리값이 같은 좌표가 여러개일 수 있기 때문에 마지막에 다시 k개까지 추출하는 것을 추가해야함.
    
# other
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0] **2 + x[1] **2)[:k]