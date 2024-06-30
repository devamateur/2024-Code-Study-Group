'''
743. Network Delay Time
https://leetcode.com/problems/network-delay-time/description/
[time] failed
[문제]  
[풀이방식]
- 
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList={i:[] for i in range(1, n+1)}
        for dep, arrival, time in times:
            adjList[dep].append((arrival, time))
            
        q=[k]
        costs=[float("inf")]*(n+1)                  # n 노드수 설정, 양의 무한대 설정
        costs[0]=costs[k]=0
        
        while q:
            departure=q.pop(0)
            for arrival, time in adjList[departure]:
                if costs[departure]+time <costs[arrival]:
                    costs[arrival]=costs[departure]+time
                    q.append(arrival)
        return -1 if any([cost==float("inf") for cost in costs]) else max(costs)



'''
failed

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        table = {}
        for dep,arr,time in times :
            if dep not in table.keys():
                table[dep] = []
            table[dep] +=[(arr,time)]

        def move(input_dep,ans):
            if input_dep not in table.keys():
                return 0, ans

            count = 0
            for a,t in table[input_dep] :
                tmp,ans =move(a,ans)
                count +=t
                ans = max(ans,count+tmp)
    
            return count,ans
        
        c,ans = move(k,0)

        return ans
        
'''