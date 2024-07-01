class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 예외 케이스, 모든 주유소를 방문할 수 없는 경우
        if sum(gas) < sum(cost):
            return -1
        idx =  0
        my_tank = 0    # 연료
        station = 0    # 시작 주유소 인덱스

        while idx < len(gas):
            # 주유소를 방문할 수 있는 경우
            if gas[idx]+my_tank >= cost[idx]:
                my_tank += gas[idx]-cost[idx]        # 주유소 연료 - 다음 주요소까지 가기 위해 필요한 연료
            else:      # 주유소를 방문할 수 없는 경우
                station = idx+1         # 다음 주유소를 시작 주유소로 설정
                my_tank = 0
            idx += 1

        return station