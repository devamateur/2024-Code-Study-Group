'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/description/
[문제] 일일 온도 : 일일 기온을 나타내는 temperatures, 더 따뜻한 날씨를 위해 며칠을 기다려야하는지 리스트로 출력

실패한 풀이(시간초과) : cur_temperature를 루프 돌면서, 미래의 온도를 비교하고 이동

cur_temperature를 루프 돌면서, 과거의 기록(idx_stack)을 비교하여 저장하는 풀이 :: 인덱스 활용
'''

### Solution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        idx_stack = []              # 인덱스 저장용

        # [73,74,71,69,72,76,73]
        for i,cur_val in enumerate(temperatures) :
            
            while idx_stack and cur_val > temperatures[idx_stack[-1]] :             # {2} if 74 > 73 : ,    {5} if 72 > 69 :,   {5} 72 > 71,    {6} 76 > 72,    {6} 76 > 71
                idx = idx_stack.pop()                                              # {2} last : 0          {5} last : 3        {5} last : 2    {6} last : 4    {6} last : 1
                ans[idx] = i-idx                                                  # {2} ans[0] : 1        {5} ans[3] : 1      {5} ans[2] : 2  {6} ans[4] : 1  {6} ans[1] : 4

            idx_stack.append(i)                                                     # {1} : [0],    {2} : [1],  {3~4} : [1,2,3],    {5} : [1,4],    {6} : [5]

        return ans



'''
time : 15m but failed
temperatures = [47,47,47,47,47,,,,,,,,]
시간 초과
왜지? two pointer 사용이 시간복잡도가 높은가??
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        left,right = 0,1
        day = 1
        result =[]

        while left < len(temperatures)-1 :
            if right >= len(temperatures):
                day = 0
            
            elif temperatures[left] >= temperatures[right] and right < len(temperatures):
                day+=1
                right +=1
                continue
            
            result.append(day)
            left +=1
            right = left+1
            day = 1
        
        result.append(0)
        return result
        
'''