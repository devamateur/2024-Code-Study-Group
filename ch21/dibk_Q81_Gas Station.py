'''
134. Gas Station
https://leetcode.com/problems/gas-station/description/

[time] failed
[문제] 원형루틴의 주유소들(n)이 있으며, 각 i번째 주유소를 이동하는 만큼의 주유량을 가진 차를 가지고 있다. 모든 곳을 방문할 수 있는 출발 인덱스를 찾기.
[풀이방식] :
- cost의 전체 합이 gas합보다 크면 무조건 -1
- gas[i]+누적연료 < cost[i]이면 이동할 수 없으므로 start,fuel 재정의
- dfs를 해야할 것 같은데 왜 이런 풀이가 나오는 지 앐 수 없당

'''
#solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start

#
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        result = -1
        size_ = len(gas)

        def calculate_circular(idx) : 

            tank = 0
            for i in range(size_):
                i = (i+idx)%size_
                tank += gas[i]-cost[i]

                if tank < 0 :
                    return False

            return True

        for i in range(size_):
            boo_ = calculate_circular(i)
            if boo_ :
                result = i
                break

        return result