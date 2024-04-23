class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path_list = []
        visited = [False]*len(nums)

        def dfs(idx):
            if len(path_list) == len(nums):
                result.append(path_list[:])      # deep copy: path_list를 그냥 append할 경우, result와 path_list가 모두 같은 값을 참조하게 됨
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    path_list.append(nums[i])
                    dfs(i+1)
                    path_list.pop()          
                    visited[i] = False

        dfs(0)

        return result