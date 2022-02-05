# greedy - 4. 만들 수 없는 금액
# 풀이 봤음
# 화폐 단위가 작은 동전부터 하나씩 확인하면서 target 변수를 업데이트 하기
n = int(input())
coins = list(map(int,input().split()))

coins.sort()
target = 1

for i in coins:
    if target < i:
        break
        
    target += i
    
print(target)