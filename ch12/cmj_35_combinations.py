class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        current = []
        visited = [False]*(n+1)

        def dfs(idx: int):
            if len(current) == k:
                result.append(current[:])       # deep copy
                return
            
            for i in range(idx, n+1):
                if not visited[i]:
                    visited[i] = True
                    current.append(i)
                    dfs(i+1)
                    current.pop()
                    visited[i] = False

        dfs(1)
        
        return result