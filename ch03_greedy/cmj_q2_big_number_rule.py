N, M, K = map(int, input().split())

nums = list(map(int, input().split()))

# 주어진 수들을 M번 더해서 가장 큰 수를 만듦
# 단, 특정 인덱스의 수가 '연속 K번' 넘게 더해질 수 없음

total_count = 0         # M 카운트
k_count = 0
result = 0
idx = 0                # nums 인덱스            

# 내림차순 정렬
nums = sorted(nums, reverse=True)

while total_count < M:
    # 항상 제일 큰 수를 K번 더하고, 두번째로 큰 수를 한 번 더하는 패턴
    result += nums[0]*K
    total_count += K
    result += nums[1]
    total_count += 1
    
print(result)