class Solution:
    def find(self, N, M):
        # 이진검색을 M번 수행하는 문제
        # 입력처리
        if N is None and M is None:
            N = int(input())

            comp = list(map(int, input().split()))           # 전체 부품
            M = int(input())
            find_comp = list(map(int, input().split()))        # 찾아야 하는 부품 번호
        else:
            # 1부터 N까지의 숫자로 구성된 전체 부품 리스트 생성
            comp = list(range(1, N + 1))

            # 무작위로 M개의 숫자를 선택하여 찾을 부품 리스트 생성
            find_comp = random.sample(range(1, 2*N), M)
            
        # 오름차순 정렬
        comp = sorted(comp)
        print('* 전체 부품 리스트\n', comp)
        print('* 찾아야 하는 부품\n', find_comp)

        result = ''
        # 이진탐색
        for i in range(len(find_comp)):
            left, right = 0, len(comp)-1
            have_items = False
            while left <= right:
                mid = (left + right)//2

                if comp[mid] == find_comp[i]:
                    have_items = True
                    break
                elif comp[mid] < find_comp[i]:
                    left = mid+1
                else:
                    right = mid-1
            if have_items:
                result += 'yes '
            else:
                result += 'no '

        return result.rstrip()
    
import random

N = 100
M = 30

s = Solution()
print('\n* 결과\n', s.find(N, M))            # s.find()