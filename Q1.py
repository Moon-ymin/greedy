s = input()
nums = list(s)
first = int(nums[0])

for i in range(1, len(nums)):
    second = int(nums[i])
    if first <= 1 or second <= 1: # 둘 중 하나라도 0이거나 1이면 더한다
        first += second
    else:
        first *= second

print(first)