# greedy - 1. 모험가 길드
# 내가 푼 방법
n = int(input())
afraid = list(map(int, input().split()))
teams = 0
afraid.sort()

# 조건문에 순서 
while True:
    if len(afraid) == 0 :
        break
    elif len(afraid) < afraid[-1] :
        break
    elif len(afraid) >= afraid[-1] :
        afraid = afraid[:len(afraid)-afraid[-1]]
        teams += 1

print(teams)

# 책에서 풀이
n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하여
    count += 1 # 현재 그룹에 해당 모험가를 포함시키자
    if count >= i : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result)