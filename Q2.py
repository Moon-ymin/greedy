# greedy - 2.곱하기 혹은 더하기
# 내가 푼 방법
s = input()
nums = list(s)         # 문자열은 굳이 리스트 형태로 안 바꿔도 됨!(생략가능)
first = int(nums[0])

for i in range(1, len(nums)):
    second = int(nums[i])
    if first <= 1 or second <= 1: # 둘 중 하나라도 0이거나 1이면 더한다
        first += second
    else:
        first *= second

print(first)