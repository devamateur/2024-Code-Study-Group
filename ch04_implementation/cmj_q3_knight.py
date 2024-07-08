loc = input()

x, y = int(loc[1]), int(ord(loc[0])-ord('a'))+1         # 열을 숫자로 변경. ord(): 문자의 아스키코드 값

# 나이트의 모든 이동 경로
move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
count = 0

for i in range(len(move)):
    new_x = x + move[i][0]
    new_y = y + move[i][1]

    # 경계값 확인
    if new_x < 1 or new_y < 1 or new_x > 8 or new_y > 8:
        continue

    count += 1

print(count)