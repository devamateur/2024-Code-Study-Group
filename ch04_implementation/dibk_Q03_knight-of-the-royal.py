'''
🍪문제 번호 :
4장 실전 문제 - 왕실의 나이트

🍈문제 정의 :
8X8크기의 체스판에서 나이트가 이동하는데, 입력값의 위치에서 체스판을 벗어나지 않는 만큼의 경우의 수를 출력하기
나이트의 이동 방향은 가로2칸+세로1칸 or 세로2칸+가로1칸 이 있다.

🍊풀이 시간 :
10분

🍒풀이 방법 :
나이트 이동 딕셔너리를 생성하고, 체스판 딕셔너리(문자열을 좌표로 바꾸기 위한)도 생성하기.
*4장 예제문제랑 같은 풀이


'''

class Solution:
    def chess(self):
        
        # 설정
        chessboard = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        knight_move = [(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        
        # 입력
        input_x,input_y = list(map(str,input("위치 입력 : ")))
        
        result = 0
        x,y = chessboard[input_x],int(input_y)
        
        for x_,y_ in knight_move :
            
            if x+x_<1 or x+x_>8 or y+y_<1 or y+y_>8 :
                # 체스판을 벗어남
                continue
                
            result +=1
        
        print("결과 : ",result)

test=Solution()
test.chess()
        