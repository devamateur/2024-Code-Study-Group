'''
🍪문제 번호 :
12장 구현 - 10 : 자물쇠와 열쇠

🍈문제 정의 :
lock배열에 빈 값을 key배열로 채울 수 있는지 확인하는 문제

🍊풀이 시간 :
failed

🍒풀이 방법 :
-자물쇠 배열에서 빈칸(0)의 위치를 찾기
각 빈칸의 상하좌우 거리(방향값도 같이)를 저장하기
- 열쇠의 값(1)의 위치 찾기
마찬가지로 각 값의 상하좌우 거리를 구하기
- 자물쇠 거리값 구한 것과 열쇠 거리값 구한 것에서 방향,거리가 맞는 게 있으면 TRUE

위 방법을 사용하려고 했는데, 생각해보니, 한 위치를 기준으로 위아래/대각선 두가지만 확인하면 되는 것 같음.
- key를 기준으로 대각선, 위아래 두 방향으로 값 저장
- lock의 빈값을 찾으면 key에서 찾은 값으로 맞춰지는 지 확인.

풀이를 찾아보니
https://sh-hyun.tistory.com/118
https://velog.io/@doyun/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC

1)배열을 90도씩 회전시키는 함수
2)key를 lock에 겹쳐지는 4방향에 대한 모든 경우를 순회하여 좌표합이 1이 되는 지 확인하는 함수..

위 2개 방법이 핵심으로 보임

이외에 프로그래머스의 다른 솔루션 참고함.

'''
# 프로그래머스 다른 솔루션
def check_match(lock, key):
    '''
    1확인하는 함수
    '''
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] + key[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key[0])
    n = len(lock[0])

    # 상하좌우 4가지 회전 향에 대한 배열을 저장함
    new_key_0 = [[0] * n for _ in range(n)]     
    new_key_1 = [[0] * n for _ in range(n)]
    new_key_2 = [[0] * n for _ in range(n)]
    new_key_3 = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            new_key_0[i][j] = key[i][j]         # 정방향
            new_key_1[j][m-i-1] = key[i][j]     # 왼쪽으로 90도 회전
            new_key_2[m-i-1][m-j-1] = key[i][j] # 뒤집어서 회전
            new_key_3[m-j-1][i] = key[i][j]     # 오른쪽으로 90도 회적

    for key in [new_key_0, new_key_1, new_key_2, new_key_3]:
        for i in range(n):                                                                 # i는 lock의 이동을 나타냄
            for j in range(n):
                left_up_key = [row[i:] + [0]*i for row in key[j:]] + [[0]*n]*j             # i==1 and new_key0 and j==0, 정방향키를 맵을 벗어난 왼쪽으로 옮긴 상태 row[i:]
                if check_match(lock, left_up_key):
                    return True
                left_down_key = [[0]*n]*(n-j-1) + [row[i:] + [0]*i for row in key[:j+1]]    # i==1 and new_key0 and j==0,
                if check_match(lock, left_down_key):
                    return True
                right_up_key = [[0]*i + row[:n-i] for row in key[j:]] + [[0]*n]*j
                if check_match(lock, right_up_key):
                    return True
                right_down_key = [[0]*n]*(n-j-1) + [[0]*i + row[:n-i] for row in key[:j+1]]
                if check_match(lock, right_down_key):
                    return True
    return False

# failed
def solution(key, lock):
    answer = True
    xlen = len(key[0])
    ylen = len(key)
    
    def distance():
        dist = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]
        for mx,my in dist :
            dx = x+mx
            dy = y+my
            
            if dx < 0 or dx > xlen or dy < 0 or dy > ylen :
                continue
    
    return answer