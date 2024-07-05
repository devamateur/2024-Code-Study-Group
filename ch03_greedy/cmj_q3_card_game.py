
N, M = map(int, input().split())

## 2차원 리스트 입력받기
nums = []

for i in range(N):
    nums.append(list(map(int, input().split())))

# 각 행에서 최소를 선택한뒤, 최소값들 중 최대를 택함

# 오름차순 정렬
for i in range(len(nums)):
    nums[i] = sorted(nums[i])

# 각 행의 최솟값 저장
row_min = []

for i in range(len(nums)):
    row_min.append(nums[i][0])

print(max(row_min))