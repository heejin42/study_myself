from collections import deque
def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(q1), sum(q2)
    for i in range(300000):
        if q1_sum == q2_sum:
            return i
        elif q1_sum > q2_sum:
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
            q2_sum += num
        else: # q2_sum이 q1_sum보다 클 때
            num = q2.popleft()
            q1.append(num)
            q2_sum -= num
            q1_sum += num      
    return -1 # 값이 같아지지 않으면 -1을 반환

    
queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]	
print(solution(queue1, queue2))