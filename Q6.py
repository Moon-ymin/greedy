# 시간이 적게 걸리는 음식부터 확인하는 그리디 사용
# 모든 음식 시간 기준으로 정리하고, 시간이 적게 걸리는 음식부터 제거하는 우선순위 큐 사용.

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같으면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 적은 음식부터 뺴야 하므로 우선순위 큐 사용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1)) # heappush() : 힙에 원소를 추가, (추가할 대상, 추가할 원소)
                                                # (음식시간, 음식번호)의 튜플 형태로 삽입
        
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k의 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length 
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정
        
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x : x[1]) # 음식의 번호 기준으로 정렬
    return result[(k-sum_value) % length][1]
    