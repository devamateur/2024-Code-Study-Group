'''
🍪문제 번호 :
5장 실전 문제 - 음료수 얼려 먹기

🍈문제 정의 :
NXM 크기의 얼음 틀에서 상하좌우로 연결된 것들을 하나의 얼음 뭉터기로 묶어서, 얼음 틀에서 얼음 뭉터기가 몇 개있는지 계산하기.

🍊풀이 시간 :
46분

🍒풀이 방법 :
상하좌우로 움직이는 좌표 딕셔너리를 생성하고, class에 결과값을 저장하는 변수를 설정한다.
얼음뭉터기를 확인하는 방법은 :
    - 얼음틀 배열의 모든 좌표를 한번씩 훝는다. 훝을 때, 값이 0인 경우만 recursive함수를 실행한다. 함수 실행이 끝나면 카운팅+1
    - recursive함수는, 좌표를 입력했을 때 해당위치에서 상하좌우로 움직이며 0인 부분을 3으로 바꾼다.
    
'''

class Solution :
    result = 0      # 결과값 초기화
    
    def iceCubes(self):
        # 입력
        N,M = map(int,input("얼음 틀의 크기 : ").split())
        ice_map = []
        for _ in range(N):
            ice_map += list(map(int,input())),

        # 설정
        move = [(0,1),(1,0),(0,-1),(-1,0)]       # 상하좌우 딕셔너리
        
        def recursive(x,y):
            ice_map[x][y] = 2       # 방문처리
            
            for x_,y_ in move :
                row = x+x_
                col = y+y_
                if row < 0 or row>=N or col<0 or col>=M or ice_map[row][col] !=0 :
                    # 얼음틀을 벗어나거나 0이 아니거나 방문했던 좌표면 실행하지 않고 넘어가기
                    continue

                recursive(row,col)
                
            return
        
        for row in range(N) :
            for col in range(M) :
                if ice_map[row][col] == 0 :
                    recursive(row,col)
                    self.result +=1
        
        print()
        print("결과 : ",self.result) 
        return 
    
test = Solution()
test.iceCubes()