N, M = map(int, input().split())

maps = []

for i in range(N):
    maps.append(list(map(int, input())))

def dfs(i, j):
    if i < 0 or i > N-1 or j < 0 or j > M-1 or maps[i][j] == 1:
        return
    
    maps[i][j] = 1   # 방문 표시

    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)

result = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)