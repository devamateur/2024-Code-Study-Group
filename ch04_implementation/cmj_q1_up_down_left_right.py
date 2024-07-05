N = int(input())
move = input().split()

# 왼쪽 상단은 (1, 1) 오른쪽 하단은 (N, N)
row, col = 1, 1

for m in move:
    new_col, new_row = col, row
    if m == 'U':
        new_row = row - 1
    if m == 'D':
        new_row = row + 1
    if m == 'R':
        new_col = col + 1
    if m == 'L':
        new_col = col - 1

    if new_row < 1 or new_row > N or new_col < 1 or new_col > N:
        continue
    row, col = new_row, new_col

print(row, col)