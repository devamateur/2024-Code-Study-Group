class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:        # 현재 온도가 스택의 top보다 더 높다면
                current = st.pop()
                result[current] = i-current
            st.append(i)     # 스택에 현재 값의 인덱스를 저장
        
        return result
    
'''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        queue = []
        result = []

        for i in range(len(temperatures)):
            queue.append(temperatures[i])

            while len(queue) >= 2 and queue[0] < queue[-1]:
                queue.pop(0)
                result.append(len(queue))

        for i in range(len(temperatures)-len(result)):
            result.append(0)

        return result
        
    아래의 경우에서 오답이 나옴
    Input
    temperatures = [73,74,75,71,69,72,76,73]

    Output [1,1,4,3,2,1,0,0]
    Expected [1,1,4,2,1,1,0,0]
'''