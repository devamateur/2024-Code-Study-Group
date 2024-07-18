'''
🍪문제 번호 :
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

🍈문제 정의 :
정렬된 nums리스트에서 두 요소 합으로 target값을 구할 수 있는 두 값의 인덱스를 구하기
*인덱스에 +1해서 리턴하기

🍊풀이 시간 :
failed, 5분

🍒풀이 방법 :
양 끝 값의 합을 비교로 포인터 이동시키기.
이전까지 mid값 구해서 포인터를 이동시키는 풀이를 활용해왔기 때문에 이 방법이 쉽게 떠오르지 않았다.

'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start,end = 0,len(numbers)-1

        while start<=end:

            if numbers[start]+numbers[end] == target :
                return [start+1,end+1]
            
            elif numbers[start]+numbers[end] > target :
                end -=1
            
            elif numbers[start]+numbers[end] < target :
                start +=1

        return -1