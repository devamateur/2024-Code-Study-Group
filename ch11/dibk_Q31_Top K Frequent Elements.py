'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/description/

[문제] 상위 k번 이상 등장하는 요소를 추출하라.
time : 10m
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for ch in nums :
            if ch not in table.keys() :
                table[ch] = 0
            table[ch] += 1
        
        table = sorted(table.items(),key = lambda x : x[1])
        ans = []

        for _ in range(k):
            key,count = table.pop()
            ans.append(key)

        return ans
    
# nums = [1,2]
# k = 2
# expected : [1,2]              << ????????
#
#
#   문제에서 k는 'k번 이상 발생한 요소'를 의미하는 것이 아니라
#   상위 k까지 도출하라는 의미...
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        for ch in nums :
            if ch not in ans.keys() :
                ans[ch] = 0
            ans[ch] += 1
        
        return [key for key,val in ans.items() if val >= k ]


