# https://ihp001.tistory.com/140
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : return 0

        volume = 0
        left,right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left<right :
            left_max, right_max = max(height[left],left_max), max(height[right],right_max)

            if left_max <= right_max :
                volume += left_max - height[left]
                left +=1
            else :
                volume += right_max - height[right]
                right -=1

        return volume

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        def find(list_):
            max_ = list_.index(max(list_))
            left = find(list_[:max_])
            right = find(list_[max_:])
            
            return 
'''