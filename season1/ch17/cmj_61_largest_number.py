class LargerNumKey(str):
    # 파이썬 비교 연산자가 내부적으로 호출하는 메소드
    def __lt__(x, y):
        # 두 수 x, y로 만들 수 있는 조합 중
        # x+y가 크다면 True를 리턴(즉, x>y)
        return x + y > y + x

class Solution:
    # 방법 1. custom comparator 이용
    def largestNumber(self, nums):
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if largest_num[0] == "0" else largest_num
    
    # 방법 2. lambda를 이용해 사전순으로 내림차순 정렬
    def largestNumber2(nums):
        # Convert all integers to strings
        nums_str = list(map(str, nums))
        
        # Define the lambda function
        key_func = lambda x: x * 10
        
        # 정렬 전
        # 3333333333, 30303030303030303030, 34343434343434343434, 5555555555, 9999999999
        print("Before sorting:")
        for num in nums_str:
            print(f'Original: {num}, Key: {key_func(num)}')   
        
        # Sort using the lambda function
        nums_str.sort(key=key_func, reverse=True)
        
        # 정렬 후
        # 9999999999 - 5555555555 - 34343434343434343434 - 3333333333 - 30303030303030303030
        print("After sorting:")
        for num in nums_str:
            print(f'Sorted: {num}, Key: {key_func(num)}')
        
        # Concatenate sorted strings
        largest_num = ''.join(nums_str)
        
        # Edge case: if the result is all zeros, return "0"
        return '0' if largest_num[0] == '0' else largest_num
