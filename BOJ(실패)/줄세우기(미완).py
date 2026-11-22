
from collections import deque

t = int(input())

for _ in range(t) :
    the_list = deque(list(map(int, input().split())))
    test_num, stu_heg = the_list[0], deque(the_list[1:])

    queue = deque([0])
    cnt = 0

    while True :

        v = stu_heg.popleft()
        if v > queue[-1] : queue.append(v)
        else :
            cnt += 1
            #보류