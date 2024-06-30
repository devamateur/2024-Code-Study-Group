class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        current = []

        def dfs(idx: int):
            if len(current) == k:
                result.append(current[:])       # deep copy
                return
            
            for i in range(idx, n+1):
                current.append(i)
                dfs(i+1)
                current.pop()

        dfs(1)
        
        return result