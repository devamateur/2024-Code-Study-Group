class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        visited = [False]*len(nums)

        def dfs(idx: int):
            
            result.append(subset[:])    # 매번 append

            for i in range(idx, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    subset.append(nums[i])
                    dfs(i)
                    subset.pop()
                    visited[i] = False

        
        dfs(0)

        return result