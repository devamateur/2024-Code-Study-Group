'''
179. Largest Number
https://leetcode.com/problems/largest-number/description/

[time] failed
[문제] 정수값의 리스트가 주어지며, 리스트의 조합으로 가장 큰 값으로 만들기(문자열로 리턴)
[풀이방식1]
- 정수 리스트를 문자열 값으로 바꾸고 정렬. 
- 정렬시, 해당 문자값을 10번 곱해서 비교(x*10 : xxxxxxxxxxx)

[풀이방식2] 답지
- 입력 리스트를 그대로 사용함. 인덱스로 값을 비교해서 교환하는 방식.
    - 인덱스로 값 비교 함수 : str(n1)+str(n2) < str(n2)+str(n1)인 경우, 리스트에서 위치 바꿈
    - while문으로 리스트 앞까지 계속 확인하며 비교.


'''
# solution1
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=lambda x: x*10, reverse=True)         # x*10 :: '3'*10 = '33333333333'
        
        if nums[0] == '0':
            return '0'
        return ''.join(nums)
    
# solution2
# nums = [3,30,34,5,9]
class Solution:
    # 문제에 적합한 비교 함수
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:                          
        return str(n1) + str(n2) < str(n2) + str(n1)

    # 삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        i = 1                                                   # 인덱스 1부터 시작 : while문의 트리거
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):     # j는 뒤에서부터 시작 : while문 트리거, n1<n2일때 위치 바뀌는 함수.
                nums[j], nums[j - 1] = nums[j - 1], nums[j]         # if j==2,  nums = [3,30,"34",5,9]
                                                                    # [3,"34",30,5,9]
                                                                    # j ==1, ["34",3,30,5,9]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))


# failed
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        tmp_dict = {}

        for num in nums :
            num = str(num)
            keyname = num[0]

            if keyname not in tmp_dict.keys():
                tmp_dict[keyname] = [num]
            
            else :
                for idx in range(len(tmp_dict[keyname])) :
                    
                    if len(tmp_dict[keyname][idx])==1 :
                        if tmp_dict[keyname][idx]+tmp_dict[keyname][idx] < num:
                            tmp_dict[keyname].insert(idx,num)
                            break
                        else :
                            tmp_dict[keyname] +=num,
                            break
                    
                    elif tmp_dict[keyname][idx] < num :
                        tmp_dict[keyname].insert(idx,num)
                        break
                else :
                    tmp_dict[keyname] +=num,
        
        result = ''
        for key in sorted(tmp_dict,reverse=True):
            result+= ''.join(tmp_dict[key])
        
        return result