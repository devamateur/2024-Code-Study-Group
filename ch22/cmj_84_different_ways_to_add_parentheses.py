class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 숫자는 그냥 리턴
        if expression.isdigit():
            return [int(expression)]
        
        result = []

        for i in range(len(expression)):
            ex = expression[i]
            if ex in '+-*':
                left = self.diffWaysToCompute(expression[:i])      # 왼쪽 숫자
                right = self.diffWaysToCompute(expression[i+1:])   # 오른쪽 숫자

                # 각 수에 대해
                for l in left:
                    for r in right:
                        if ex == '+':
                            result.append(l+r)
                        elif ex == '-':
                            result.append(l-r)
                        elif ex == '*':
                            result.append(l*r)

        return result