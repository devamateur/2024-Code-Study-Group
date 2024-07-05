N, K = map(int, input().split())
op_count = 0       # 연산횟수

while N != 1:
    # K로 나눠떨어지는 경우 N을 K로 나눔
    if N%K == 0:
        N //= K
        op_count += 1
    else:
        N -= 1
        op_count += 1

print(op_count)