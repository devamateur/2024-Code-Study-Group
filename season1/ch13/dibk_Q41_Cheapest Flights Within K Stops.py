'''
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
[time] failed
[문제]  
[풀이방식]
- 
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjTable = {i:[] for i in range(n+1)}
        for dep,arr,price in flights :
            adjTable[dep].append([arr,price])
        
        q = [(src,0,0)]                 # 출발지, 누적가격, 뎁스
        costs=[float('inf')]*n
        
        while q:
            departure,cum_price,depth = q.pop(0)  # 출발지, 누적가격, 뎁스
   
            if depth > k : continue
            
            for arrival, price in adjTable[departure] :
                cost = cum_price + price            # 누적가격+가격
                if costs[arrival] > cost :          # costs[arrival] == float('inf') 인 경우, 설정
                    costs[arrival] = cost
                    q.append((arrival,cost,depth+1))
        
        return -1 if costs[dst]==float('inf') else costs[dst]
    

# failed
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjTable = {}
        for dep,arr,price in flights :
            if dep not in adjTable.keys():
                adjTable[dep] = []
            adjTable[dep].append([arr,price])
        
        q = [(src,0)]
        costs=[0]*n
        k +=1

        while k:
            dep,pre_price = q.pop(0)
   
            for arr,price in adjTable[dep] :
                costs[arr] = price +pre_price
                q.append((arr,costs[arr]))

            k-=1

        return costs[dst]