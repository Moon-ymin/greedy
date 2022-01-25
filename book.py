# 3-1.py 답안 예시
# 거스름돈 -> 그리디 ? 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 큰 수의 법칙
# 1. m이 100000이하인 경우
n, m, k = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort(reverse = True) # 입력받은 수 내림차순 정렬
first = nums[0]
second = nums[1]
total = 0

while True:
    for i in range(k):
        if m == 0:
            break
        total += first
        m -= 1
    
    if m == 0:
        break
    total += second
    m -= 1

print(total)

# 2. m의 크기가 100억 이상일 때 - 반복되는 수열을 파악해서 계산하는 방법
n, m, k = map(int,input().split())
nums = list(map(int, input().split()))

nums.sort(reverse = True)
first = nums[0]
second = nums[1]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1) # m이 k+1로 나누어 떨어지지 않는 경우

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)

# 숫자 카드 게임
# 내가 푼 것 - 리스트 정렬 이용
n, m = map(int,input().split())
min_nums = []

for i in range(n):
    li = list(map(int,input().split()))
    li.sort()
    min_nums.append(li[0])

print(max(min_nums))

# 1. min() 함수 이용
n,m = map(int,input().split())
result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int,input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

# 2. 2중 반복문 구조를 이용하는 답안
n,m = map(int,input().split())
result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int,input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
        
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

# 1이 될 때까지
# 1. 단순 답안
n, k = map(int, input().split())
times = 0
# n이 k이상이라면 k로 계속 나누기
while n >= k:
    # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0:
        n -= 1
        times += 1
    # k로 나누기
    n //= k
    times += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    times += 1

print(times)

# 2. n이 엄청 클 경우
n, k = map(int,input().split())
result = 0

while True:
    # (n == k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)