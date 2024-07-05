'''
문제 번호 :
3장 실전 문제 3 : 숫자 카드 게임

문제 정의 :
여러 개의  숫자 카드 중 가장 높은 숫자를 한 장 뽑는 게임
카드는 NXM형태로 놓여 있고, 우선 행을 선택 후 그 행에서 가장 낮은 숫자의 카드를 뽑는다.
따라서 행을 선택할 때, 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

풀이 시간 : 
6분

풀이 방법 :
각 행의 가장 작은 값을 임의의 변수에 담고, 그 변수 내에서 가장 큰 값을 찾기.

'''

class Solution :
    def card_game(self) -> None :
        n,m = map(int,input('행, 열 입력하기(공백기준) : ').split())

        result = []
        print('카드의 숫자 입력하기(공백기준) : ')
        for _ in range(n):
            cards = list(map(int,input().split()))
            result += min(cards),

        print()
        print("## 결과 : ",max(result))
    
        return

test = Solution()
test.card_game()

