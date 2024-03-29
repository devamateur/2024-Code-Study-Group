'''
time : 25m but failed
시간 초과
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []

        left,right = 0, 1
        day = 1

        while left < len(temperatures)-1 :
            if right >= len(temperatures) :
                day = 0

            elif temperatures[left] >= temperatures[right] :
                right +=1
                day +=1
                continue

            ans.append(day)
            left +=1
            right = left+1
            day = 1

        if left < len(temperatures) :
            for _ in range(len(temperatures)-left):
                ans.append(0)
                
        return ans
        
'''