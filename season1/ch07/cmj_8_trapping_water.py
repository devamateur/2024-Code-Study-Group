class Solution:
    def trap_brute_force(self, height: List[int]) -> int:
        ''' 처음 한 생각 
            물이 고이려면 값이 내림차순 or 오름차순이면 안됨
            반드시 상하상 형태여야 함
            상하상: 상들 중에서 최솟값 택함
            
            이렇게 생각해서 물이 고이는 범위를 인덱스로 나타내기가 어려웠음
            그런데 사실 상하상 형태에서 최솟값을 택하는 아이디어가
            바로 왼쪽 최대값과 오른쪽 최대값 사이에서 최소를 택하는 것과 같기 때문에
            투포인터를 바로 떠올릴 수 있었다면 풀 수 있었을 것 같다..
        '''

        if not height:            # heigt의 원소 수는 정수이므로 0도 포함됨
            return 0
        
        waters = 0

        # 이 방법은 O(n2)이므로 time limit이 발생함
        for i in range(len(height)):
            max_left, max_right = 0, 0

            for j in range(i, len(height)):          # 왼쪽 부분에서 max
                max_left = max(max_left, height[j])
            
            for j in range(i+1):                     # 오른쪽 부분에서 max
                max_right = max(max_right, height[j])

            waters += min(max_left, max_right)-height[i]             # 물이 고이는 높이 = 왼쪽/오른쪽 중 최솟값과 현재 높이의 차
            
        return waters


        
    def trap_2pointer(self, height: List[int]) -> int:
        
        if not height:       
            return 0

        waters = 0
        left, right = 0, len(height)-1

        max_left = height[left]
        max_right = height[right]

        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            print(left, right, max_left, max_right, waters)

            if max_left <= max_right:         # 더 큰쪽으로 포인터 이동
                waters += max_left - height[left]
                left += 1
            else:
                waters += max_right - height[right]
                right -= 1

        return waters