# greedy - 5. 볼링공 고르기
# 첫 번째 푼 방법  
n, m = map(int,input().split())
weights = list(map(int,input().split()))

choice = 0

for i in range(len(weights)):
    for j in weights[i+1:]:
        if weights[i] != j :
            choice += 1

print(choice)

# 두 번째 푼 방법 (파이썬 함수 사용)
from itertools import combinations # 파이썬 모듈 combinations 사용 

n,m = map(int,input().split())
weights = list(map(int,input().split()))

numbers = list(combinations(weights, 2))

# print(numbers[0][0],numbers[0][1]) --> 1 3

for i in range(len(numbers)):
    if (numbers[i][0]) == (numbers[i][1]):
        del numbers[i] 
        
print(len(numbers))

# error : numbers 리스트 내부 값이 같을 때, del로 numbers 리스트 내부 값이 없어지면 
# 인덱스로 따지는 과정에서 out of range 오류가 발생한다.
# if 조건문에서 numbers 리스트 안의 숫자들이 다를때, 최종 리스트에 추가하는 방식으로 함수를 바꾸기로 했다.

# 수정
from itertools import combinations # 파이썬 모듈 combinations 사용 

n,m = map(int,input().split())
weights = list(map(int,input().split()))

numbers = list(combinations(weights, 2))

# print(numbers[0][0],numbers[0][1]) --> 1 3

final = []

for i in range(len(numbers)):
    if (numbers[i][0]) != (numbers[i][1]):
        final.append(numbers[i])
        
print(len(final))

# 교재 답안
# 무게마다 볼링공의 개수부터 계산
n,m = map(int,input().split()) # 5,3
data = list(map(int,input().split())) # 1 3 2 3 2 

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1 # [0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0]
    
result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기
    
print(result) 

"""
i n result + array[i] * n // result
1 4 0 + 1 * 4 // 4
2 2 4 + 2 * 2 // 8
3 0 8 + 2 * 0 // 8
"""
