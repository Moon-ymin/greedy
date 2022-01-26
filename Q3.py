# greedy - 3. 문자열 뒤집기
# 내가 푼 방법
def solution(s):
    result = []
    result.append(s[0])
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            result.append(s[i])
    return result

s = input()
new_s = solution(s)

cnt0 = 0
cnt1 = 0

for i in new_s:
    if i == '0':
        cnt0 += 1
    else:
        cnt1 += 1

print(min(cnt0,cnt1))

# 교재 답안
data = input()
cnt0 = 0 # 전부 0으로 바꾸는 경우
cnt1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    cnt0 += 1
else:
    cnt1 += 1
    
# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i+1] == '1':
            cnt0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            cnt1 += 1
            
print(min(cnt0,cnt1))