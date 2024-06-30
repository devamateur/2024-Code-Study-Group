'''
332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/description/
[time] Failed
[문제] 링크참고
[풀이방식]
- 
'''

# failed Solution
# tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# Output = ["JFK","KUL"]
# Expected = ["JFK","NRT","JFK","KUL"]
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # step1
        itinerary = {}
        for k,v in tickets :
            if k not in itinerary.keys():
                itinerary[k] = []
            
            itinerary[k] +=[v]
            itinerary[k] = sorted(itinerary[k],reverse=True)
        
        # step2
        from_key = "JFK"
        ans =[]
        ans +=[from_key]
        
        while from_key in itinerary.keys() and itinerary[from_key] :
            to_key = itinerary[from_key].pop()
            ans.append(to_key)
            from_key = to_key

        return ans