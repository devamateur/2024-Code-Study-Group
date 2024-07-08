'''
🍪문제 번호 :
5장 실전 문제 - 미로 탈출

🍈문제 정의 :
NXM 크기의 미로. 시작의 위치는 (1,1)==(좌표 : 0,0)이며 미로의 도착 위치는 (N,M)이다.
괴물이 없는 1부분으로 위치를 이동하며 도착지로 무사히 도착해야한다. 최소 이동 칸의 갯수를 계산하기.

🍊풀이 시간 :
1시간 10분

🍒풀이 방법 :
*음료수 얼려먹기 문제와 비슷한 풀이방식, but BFS

상하좌우로 움직이는 좌표 데큐를 생성한다. 단, 오-밑-왼-위 순으로 이동하게 한다.
그리고 이미 움직인 방향의 좌표는 임시데큐에 넣어둔다. 
class에 결과값을 저장하는 변수를 설정한다.



*issue
- 이동좌표는 row,col로 초기화, while문에서 row,col에 업데이트가 안되는 현상이 발생함 :: 이 문제를 해결하는데 40분 걸림ㅠ
    - row,col을 이동 좌표로 설정 후, move좌표의 x,y를 row+x, col+=y로 설정함 : 이 부분이 오류를 발생시킴
        - while문에서 row를 업데이트하지 않고 바로 if문에서 위와같이 진행을하면 x,y 업데이트가 꼬이는 현상 확인됨.
    - 이동좌표를 x,y로 설정, move좌표를 x_,y_, 이동하게 되는 좌표위치를 row,col로 변경하여 진행
        
    
'''
from collections import deque
class Solution :
    result = 0      # 결과값 초기화
    
    def maze(self):
        # 입력
        N,M = map(int,input("미로 크기 : ").split())
        maze_map = []
        for _ in range(N):
            maze_map += list(map(int,input())),

        # 설정
        move = deque([(0,1),(1,0),(0,-1),(-1,0)]) # 오른쪽 아래 왼쪽 위
        tmp = []                                  # move의 popleft값을 임시로 담아두는 공간
        
        def run():
            x,y = 0,0       # 미로에서 시작점
            self.result +=1     # 시작칸 포함
            
            while move :
                x_,y_ = move.popleft()
                
                row = x+x_
                col = y+y_
                
                if row<0 or row>=N or col<0 or col>=M or maze_map[row][col]!=1:
                    tmp.append((x_,y_))           # 해당 이동은 tmp에 임시로 저장해두기
                    continue
   
                self.result +=1
                x,y = row,col                   # 갱신
                
                move.appendleft((x_,y_))          # 해당 이동을 먼저 move에 넣고, tmp의 뒤에서부터 move에 넣는다.
                for i in tmp[::-1]:
                    move.appendleft(i)

                
                if row == N-1 and col == M-1 :
                    # 도착지점에 도달함.
                    break
            
            return

        # 실행
        run()        
        print()
        print("결과 : ",self.result) 
        return 
    
test = Solution()
test.maze()